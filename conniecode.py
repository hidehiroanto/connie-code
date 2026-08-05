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
        payload = {"scope": "topics" if not self.session_id else "followup", "prompt": prompt}
        if self.session_id and self.owner_token:
            payload["sessionId"], payload["ownerToken"] = self.session_id, self.owner_token

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
                            try:
                                event = json.loads(chunk[len("data: "):])
                                event_type = event.get("type")

                                if event_type == "session":
                                    self.owner_token, self.session_id = event.get("ownerToken"), event.get("sessionId")
                                elif event_type == "topic":
                                    pass
                                elif event_type == "token":
                                    print(event.get("token", ""), end="", flush=True)
                                elif event_type == "error":
                                    print(f"\n[API Error]: {event.get("error", "Unknown error")}")

                            except json.JSONDecodeError:
                                pass
                print()
        except HTTPError as e:
            print(f"\n[HTTP Error {e.code}]: {e.reason}")
        except URLError as e:
            print(f"\n[Connection Error]: {e.reason}")

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
