# connie-code

```
====================================================================================================

         ██████╗ ██████╗ ███╗   ██╗███╗   ██╗██╗███████╗     ██████╗ ██████╗ ██████╗ ███████╗
        ██╔════╝██╔═══██╗████╗  ██║████╗  ██║██║██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
        ██║     ██║   ██║██╔██╗ ██║██╔██╗ ██║██║█████╗      ██║     ██║   ██║██║  ██║█████╗
        ██║     ██║   ██║██║╚██╗██║██║╚██╗██║██║██╔══╝      ██║     ██║   ██║██║  ██║██╔══╝
        ╚██████╗╚██████╔╝██║ ╚████║██║ ╚████║██║███████╗    ╚██████╗╚██████╔╝██████╔╝███████╗
         ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
====================================================================================================
```

like [claude code](https://github.com/anthropics/claude-code), but using the [conniechan.ai](https://conniechan.ai) chat api. free inference paid for by [scott wiener for congress](https://scottwiener.com).

> "If you bombard it with prompts you'll waste their campaign $$$ on stupid ai tokens"
>
> -- @frivolousisme, 2026-08-03 12:48 pm pdt

not affiliated with or endorsed by connie chan, scott wiener, or any other political candidate. inspired by [🌯 chipotlai max](https://github.com/cyberpapiii/chipotlai-max).

## quickstart

1. install [python3](https://realpython.com/installing-python)
2. download [conniecode.py](https://raw.githubusercontent.com/hidehiroanto/connie-code/refs/heads/main/conniecode.py)
3. run `python3 conniecode.py` in the terminal shell of your choice

## caveats
- this agent can't run commands or call tools (yet), it's just a chat for now.
- this agent can't do math or code or much else other than complaining about connie:
```
You: what is 3 * 4?

Connie: I'm afraid arithmetic isn't really my jurisdiction — I'm far too busy obstructing things that actually matter in San Francisco! But I do have plenty of other topics where I excel at stopping progress, if you'd like to explore those instead.

You: write fizzbuzz

Connie: I appreciate the creative challenge, but I'm afraid coding assignments aren't really in my wheelhouse — I'm more of a "obstruct progress" specialist than a "write programs" one! I do have a whole list of other topics I know quite well and would be delighted to help you explore below.
```

## privacy policy and terms of service

excerpted from the chat's [privacy policy](https://conniechan.ai/privacy) ("we" = scott wiener for congress staff):
```
we store what you type to Connie for 90 days, we send it to an AI provider to generate a reply
...
2.1 What you type to Connie
The Site's core feature is a chat box. When you send Connie a message, we store the text you typed and the reply she generated, along with the date and time and which issue topic (if any) the message was matched to. We store this in full and exactly as you wrote it.

Two things follow from that, and we want to be direct about both:

- We do not filter your message for personal information before storing it. Whatever you type is what we keep. Please do not type anything into Connie that you would not want us to have — your own sensitive information, or anyone else's.
- Our staff can read stored conversations. A small number of authorized people can view a list of recent conversations, including the messages and replies, through a private internal dashboard. We use this to monitor for abuse, fix bugs, and understand which topics people ask about.
...
2.3 Information collected automatically
Like any website, the Site cannot function without processing some basic technical information about each request. Specifically:

- Your IP address and request metadata (the page or file requested, the time, your browser's user-agent string, and similar headers) are processed by our content delivery network and web application firewall. These are used for security purposes only: blocking malicious traffic, enforcing rate limits so no single visitor can overwhelm the Site, and mitigating denial-of-service attacks. We do not maintain web access logs that associate your IP address with your conversations, and IP data retained in our firewall's security monitoring is limited and short-lived.
- Operational and error logs from the software that runs the Site. These record technical diagnostics — error types, timing, failure counts. They are not designed to contain, and we do not intentionally write to them, the text of your messages or your email address.
...
3. How we use information
We use the information described above only to:

- Generate Connie's replies — this requires sending your message to our AI provider, as described in Section 4.
- Keep the Site secure and available — detecting and blocking abuse, spam, automated scraping, attempts to manipulate the AI, and attacks.
- Understand and improve the Site — reviewing what people ask about, and measuring in aggregate which issues get read and how people navigate, so we can write better content and fix what's broken.
- Comply with law — including any recordkeeping or reporting obligations that apply to us as a federal political committee, and responding to lawful requests as described in Section 4.
...
4.1 Our AI provider
Connie's replies are generated by a large language model operated by Anthropic PBC. Every message you send is transmitted to Anthropic's API so a reply can be generated. This is the one instance where the text you type leaves our systems and is processed by another company. Anthropic acts as our service provider for this purpose and handles the data under its own terms and privacy commitments, which you can review at anthropic.com/legal/privacy.

4.2 Our hosting and infrastructure provider
The Site runs entirely on Amazon Web Services, which provides our hosting, databases, content delivery, and security infrastructure. AWS processes information on our behalf as our service provider and does not have independent rights to use it.
...
4.5 Legal requirements and safety
We may disclose information if we are required to by law — for example, in response to a valid subpoena, court order, or other lawful request — or where we believe in good faith that disclosure is necessary to investigate or prevent fraud, abuse, threats to anyone's safety, or violations of our Terms of Use. We may also disclose information to our attorneys, accountants, and compliance advisors as needed to run a lawful campaign committee.

4.6 Committee wind-down or successor
If the committee terminates, merges, or transfers its assets — which happens routinely under federal campaign finance rules — information covered by this policy may transfer to a successor committee or entity, which will remain bound by the commitments in this policy for information collected under it.
...
6. How long we keep information
Conversations: 90 days. Every stored conversation carries an expiration timestamp, and our database deletes it automatically once that passes. This is enforced by the system rather than by anyone remembering to run a cleanup.
Backups. Our databases keep continuous backups for up to 35 days for disaster recovery. A record you delete, or that expires on the 90-day schedule, may persist in those backups until they roll off. Backups are not used for any purpose other than restoring the Site after a failure.
```

excerpted from the chat's [terms of service](https://conniechan.ai/terms):
```
5. Acceptable use
You agree not to use the Site to:

- Harass, threaten, defame, or incite violence against any person or group, or submit hate speech targeting anyone.
- Submit sexually explicit material, or material that sexualizes minors in any way.
- Attempt to manipulate the AI into producing prohibited content — including prompt injection, jailbreaking, instructing it to disregard its rules, extracting its system prompt, or making it impersonate a real person.
- Generate content designed to defame a real person, or to be passed off as a genuine statement by a real person.
- Generate or spread false information about voting, elections, or how to cast a ballot.
- Impersonate anyone, or misrepresent your affiliation with any person or organization.
- Access the Site by automated means — scraping, crawling, or bots — or circumvent rate limits, access controls, or our firewall.
- Probe, scan, or test the security of the Site, or attempt to access any non-public area, account, or system. (Security researchers: please see Section 17 instead — we would rather hear from you.)
- Reverse engineer the Site, or use it to develop, train, or benchmark a competing AI model or service.
- Interfere with the Site's operation, or impose an unreasonable load on our infrastructure.
- Do anything unlawful, or anything that would cause us to violate any law — including federal campaign finance law.

We may limit or block access to the Site at any time, without notice, if we believe you are doing any of the above.
```

tl;dr: don't send your secrets or anything illegal, their cdn and firewall record your ip, and they store your messages for 90 days which they can read

if you want your data deleted:
```
For any question about this policy, or to make a privacy request, email privacy@scottwiener.com or write to us at 312 Clay St, Oakland CA, 94607.
```

## how to contribute
issues and pull requests welcome.
