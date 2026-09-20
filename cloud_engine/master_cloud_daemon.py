"""
MASTER CLOUD DAEMON (24/7 AUTONOMOUS REVENUE ENGINE)
Runs on GitHub Actions Cloud Runners with 0 VNĐ cost.
Operates indefinitely even when the user's local computer is completely powered off.
"""

import os
import sys
import json
import time
import urllib.request
import subprocess
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ENGINE_DIR = os.path.join(CURRENT_DIR, "engine")
AGENT_DIR = os.path.join(CURRENT_DIR, "autonomous_agent")
if ENGINE_DIR not in sys.path:
    sys.path.insert(0, ENGINE_DIR)

from autonomous_orchestrator import run_pipeline

def get_github_token():
    # 1. Check environment variable (used by GitHub Actions)
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        return token
    
    # 2. Check git credentials (used locally)
    try:
        p = subprocess.Popen(['git', 'credential', 'fill'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        out, _ = p.communicate('protocol=https\nhost=github.com\n')
        for line in out.splitlines():
            if line.startswith('password='):
                return line.split('password=', 1)[1].strip()
    except Exception:
        pass
    return ""

def check_bounty_payouts(headers, ledger):
    print("\n[CLOUD DAEMON] 1. Kiểm tra đối soát giải ngân tự động trên các nền tảng...")
    
    # Check MergeEarn PR 43 & 45
    for pr_id in [43, 45]:
        try:
            url = f'https://api.github.com/repos/Saidur-droid/MergeEarn/pulls/{pr_id}'
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode())
                is_merged = data.get('merged', False)
                print(f"  * Saidur-droid/MergeEarn PR #{pr_id}: State={data.get('state')}, Merged={is_merged}")
                if is_merged:
                    print(f"    🎉 PR #{pr_id} ĐÃ ĐƯỢC MERGE! KÍCH HOẠT PHÂN PHỐI NIM!")
                    ledger['actual_revenue']['NIM'] = max(ledger.get('actual_revenue', {}).get('NIM', 0), 20)
        except Exception as e:
            print(f"    Lỗi kiểm tra MergeEarn PR #{pr_id}:", e)

    # Check RustChain PR 16999 & Issue 16997
    try:
        url = 'https://api.github.com/repos/Scottcjn/rustchain-bounties/pulls/16999'
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            is_merged = data.get('merged', False)
            print(f"  * RustChain Wallet PR #16999: State={data.get('state')}, Merged={is_merged}")
    except Exception as e:
        print("    Lỗi kiểm tra RustChain PR 16999:", e)

    # Check RustChain main issue #302 (Blog post)
    try:
        url = 'https://api.github.com/repos/Scottcjn/Rustchain/issues/302/comments?per_page=3&sort=created&direction=desc'
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            comments = json.loads(resp.read().decode())
            for c in comments:
                body = c.get('body', '').lower()
                if any(w in body for w in ['approved', 'payout', 'sent', 'paid', 'merged', 'reward sent']):
                    print(f"    ⭐ Thông báo thanh toán/phê duyệt phát hiện tại Rustchain #302 bởi {c['user']['login']}: {c['body'][:100]}...")
    except Exception:
        pass

    # Check RustChain bounty issues
    issues = [1524, 1098, 1577, 1579, 14476, 16998, 16863, 478]
    for iss in issues:
        try:
            url = f'https://api.github.com/repos/Scottcjn/rustchain-bounties/issues/{iss}/comments?per_page=3&sort=created&direction=desc'
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                comments = json.loads(resp.read().decode())
                for c in comments:
                    body = c.get('body', '').lower()
                    if any(w in body for w in ['approved', 'payout', 'sent', 'paid', 'merged', 'reward sent']):
                        print(f"    ⭐ Thông báo thanh toán/phê duyệt phát hiện tại RustChain #{iss} bởi {c['user']['login']}: {c['body'][:100]}...")
        except Exception:
            pass

def main():
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=" * 70)
    print(f">>> ☁️ MASTER CLOUD DAEMON ĐANG CHẠY TRÊN GITHUB ACTIONS (24/7) <<<")
    print(f">>> Thời gian khởi chạy: {start_time}")
    print("=" * 70)

    token = get_github_token()
    headers = {'Authorization': f'token {token}', 'User-Agent': 'CloudBountyHunter'} if token else {'User-Agent': 'CloudBountyHunter'}

    ledger_path = os.path.join(AGENT_DIR, "ledger.json")
    ledger = {}
    if os.path.exists(ledger_path):
        try:
            with open(ledger_path, "r", encoding="utf-8") as f:
                ledger = json.load(f)
        except Exception:
            pass

    # 1. Check live settlement
    check_bounty_payouts(headers, ledger)

    # 2. Run the Autonomous Orchestrator pipeline
    print("\n[CLOUD DAEMON] 2. Kích hoạt chu kỳ Autonomous Orchestrator...")
    run_pipeline()

    # 3. Update ledger timestamp and status
    ledger["last_cloud_run"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ledger["cloud_runner"] = "GitHub Actions 24/7 Autonomous Agent"
    
    with open(ledger_path, "w", encoding="utf-8") as f:
        json.dump(ledger, f, ensure_ascii=False, indent=2)
        
    print(f"\n[CLOUD DAEMON] Đã cập nhật sổ cái ledger.json tại: {ledger_path}")
    print("=" * 70)
    print(">>> ☁️ CHU KỲ CLOUD HOÀN TẤT - TIẾP TỤC ĐỢI CHU KỲ CRON TIẾP THEO <<<")
    print("=" * 70)

if __name__ == "__main__":
    main()
