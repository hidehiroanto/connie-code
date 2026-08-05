#!/usr/bin/env python3

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API_URL = "https://conniechan.ai/api/match"

LOGO = """\x1b[38;5;208m
     ██████╗ ██████╗ ███╗   ██╗███╗   ██╗██╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗
    ██╔════╝██╔═══██╗████╗  ██║████╗  ██║██║██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
    ██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║██║█████╗      ██║     ██║   ██║██║  ██║█████╗
    ██║     ██║   ██║██║╚██╗██║██║╚██╗██║██║██╔══╝      ██║     ██║   ██║██║  ██║██╔══╝
    ╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║██║███████╗    ╚██████╗╚██████╔╝██████╔╝███████╗
     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
\033[0m"""

class ConnieAgent:
    def __init__(self):
        self.session_id = None
        self.owner_token = None

    def ask(self, prompt: str):
        payload = {
            "scope": "topics" if not self.session_id else "followup",
            "prompt": prompt
        }
        if self.session_id and self.owner_token:
            payload["sessionId"] = self.session_id
            payload["ownerToken"] = self.owner_token

        req = Request(API_URL, json.dumps(payload).encode(), {"Content-Type": "application/json"}, method="POST")

        try:
            with urlopen(req) as resp:
                buffer = ""
                print("\nConnie: ", end="", flush=True)

                for line_bytes in resp:
                    buffer += line_bytes.decode()

                    while "\n\n" in buffer:
                        chunk, buffer = buffer.split("\n\n", 1)
                        chunk = chunk.strip()
                        if chunk.startswith("data: "):
                            raw_json = chunk[6:]
                            try:
                                self._process_event(json.loads(raw_json))
                            except json.JSONDecodeError:
                                pass
                print()
        except HTTPError as e:
            print(f"\n[HTTP Error {e.code}]: {e.reason}")
        except URLError as e:
            print(f"\n[Connection Error]: {e.reason}")

    def _process_event(self, event: dict):
        event_type = event.get("type")

        if event_type == "session":
            self.session_id = event.get("sessionId")
            self.owner_token = event.get("ownerToken")
        elif event_type == "topic":
            pass
        elif event_type == "token":
            token = event.get("token", "")
            print(token, end="", flush=True)
        elif event_type == "error":
            error_msg = event.get("error", "Unknown error")
            print(f"\n[API Error]: {error_msg}")

def main():
    agent = ConnieAgent()
    print("=" * 94)
    print(LOGO)
    print("Type '/exit' or '/quit' to exit.")
    print("=" * 94)

    while True:
        try:
            prompt = input("\nYou: ").strip()
            if not prompt:
                continue
            if prompt.lower() in ("/exit", "/quit"):
                print("Goodbye!")
                break
            agent.ask(prompt)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            sys.exit(0)

if __name__ == "__main__":
    main()
