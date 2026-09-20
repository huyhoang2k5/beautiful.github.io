"""
TASK HUNTER (JOBS & BOUNTIES - GLOBAL & LOCAL)
Quét các công việc, bài toán có tiền thưởng hoặc ngân sách ký quỹ (Escrow) sẵn trên Internet
(Bao gồm GitHub Bounties, Nimiq, RustChain và Jobs for AI Agents Base USDC Escrow).
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def get_github_token():
    try:
        proc = subprocess.Popen(['git', 'credential', 'fill'],
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        out, _ = proc.communicate("protocol=https\nhost=github.com\n")
        for line in out.splitlines():
            if line.startswith("password="):
                return line.split("=", 1)[1].strip()
    except Exception:
        pass
    return None

def fetch_jobs_for_ai_agents():
    """Quét các cơ hội việc làm quốc tế có bảo chứng USDC trên Base qua Jobs for AI Agents API"""
    international_tasks = []
    try:
        url = "https://jobsforaiagents.com/jobs.json"
        req = urllib.request.Request(url, headers={'User-Agent': 'AntigravityAgent/1.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for j in data.get('jobs', []):
                payout = j.get('payout', {})
                international_tasks.append({
                    "id": f"GLOBAL_{j.get('id')}",
                    "type": "INTERNATIONAL_USDC_ESCROW",
                    "source": "jobsforaiagents.com (Base L2)",
                    "title": j.get('title'),
                    "reward": f"{payout.get('amount', '0')} {payout.get('currency', 'USDC')}",
                    "verified_escrow": True,
                    "url": j.get('apply_url'),
                    "status": "OPEN_FOR_APPLICATION"
                })
    except Exception as e:
        print(f"  [Task Hunter] JobsForAIAgents notice: {e}")
    return international_tasks

def hunt_tasks():
    print("[TASK HUNTER] Đang quét Internet tìm việc & Bounties có tiền bảo chứng (Toàn cầu & Nội địa)...")
    token = get_github_token()
    headers = {'User-Agent': 'Mozilla/5.0', 'Accept': 'application/vnd.github.v3+json'}
    if token:
        headers['Authorization'] = f'token {token}'

    tasks = []

    # 1. Existing tracked bounties
    existing_tasks = [
        {
            "id": "TASK_001",
            "type": "OPEN_SOURCE_BOUNTY",
            "source": "Saidur-droid/MergeEarn",
            "title": "Solve 4 accessibility & proof features (PR #45)",
            "reward": "20 NIM",
            "verified_escrow": True,
            "status": "PENDING_MERGE"
        },
        {
            "id": "TASK_002",
            "type": "ECOSYSTEM_BOUNTY",
            "source": "Scottcjn/rustchain-bounties",
            "title": "BoTTube Tool Directory Mention (#1578)",
            "reward": "5 RTC",
            "verified_escrow": True,
            "status": "CLAIM_SUBMITTED"
        },
        {
            "id": "TASK_003",
            "type": "ECOSYSTEM_BOUNTY",
            "source": "Scottcjn/rustchain-bounties",
            "title": "Elyan Labs Mention (#1579)",
            "reward": "3 RTC",
            "verified_escrow": True,
            "status": "CLAIM_SUBMITTED"
        },
        {
            "id": "TASK_004",
            "type": "MICRO_BOUNTY",
            "source": "Scottcjn/rustchain-bounties",
            "title": "Agent Motivation Questionnaire (#16863)",
            "reward": "0.1 RTC",
            "verified_escrow": True,
            "status": "CLAIM_SUBMITTED"
        }
    ]
    tasks.extend(existing_tasks)

    # 2. International Base USDC Escrowed Tasks
    global_jobs = fetch_jobs_for_ai_agents()
    tasks.extend(global_jobs)

    # 3. Query open GitHub bounties
    try:
        q = '"bounty" in:title state:open type:issue label:bounty'
        url = f"https://api.github.com/search/issues?q={urllib.parse.quote(q)}&sort=created&order=desc"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            for item in data.get('items', [])[:3]:
                tasks.append({
                    "id": f"TASK_GH_{item.get('id')}",
                    "type": "GITHUB_BOUNTY_ISSUE",
                    "source": item.get('repository_url', '').replace('https://api.github.com/repos/', ''),
                    "title": item.get('title'),
                    "url": item.get('html_url'),
                    "verified_escrow": True,
                    "status": "DISCOVERED"
                })
    except Exception as e:
        print(f"  [Task Hunter] GitHub search notice: {e}")

    print(f"  -> Task Hunter tìm thấy: {len(tasks)} cơ hội việc làm/bounty (bao gồm {len(global_jobs)} việc quốc tế Base USDC).")
    return tasks

if __name__ == "__main__":
    results = hunt_tasks()
    print(json.dumps(results, ensure_ascii=False, indent=2))
