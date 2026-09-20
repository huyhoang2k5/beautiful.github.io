import urllib.request
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

for n in [28, 27, 26]:
    url = f"https://api.github.com/repos/Saidur-droid/MergeEarn/issues/{n}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print("=" * 60)
            print(f"ISSUE #{n}: {data.get('title')}")
            print(f"URL: {data.get('html_url')}")
            print("-" * 60)
            print(data.get('body'))
            print("=" * 60 + "\n")
    except Exception as e:
        print(f"Loi #{n}:", e)
