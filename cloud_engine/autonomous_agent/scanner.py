"""
AUTONOMOUS MONEY-SEEKING AGENT - SCANNER MODULE
Quét liên tục các nguồn cơ hội kiếm tiền 0 đồng thực tế:
1. GitHub Issue Bounties (Algora, Opire, Polar.sh)
2. Open Source Paid Tasks
3. High-demand Micro-services & Data Requests
"""

import urllib.request
import urllib.parse
import json
import os
import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, "discovered_opportunities.json")

def search_github_bounties():
    print("[1/3] Quét GitHub Bounties thực tế (Algora, Opire, Polar)...")
    queries = [
        'is:issue is:open label:bounty "algora" comments:<10',
        'is:issue is:open "app.opire.dev" comments:<10',
        'is:issue is:open label:bounty "polar.sh" comments:<10',
        'is:issue is:open label:"help wanted" "bounty" comments:<5'
    ]
    
    bounties = []
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for q in queries:
        url = f"https://api.github.com/search/issues?q={urllib.parse.quote(q)}&sort=created&order=desc"
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode())
                items = data.get("items", [])
                for item in items[:5]:
                    repo_name = item.get("repository_url", "").replace("https://api.github.com/repos/", "")
                    bounties.append({
                        "type": "CODE_BOUNTY",
                        "title": item.get("title"),
                        "repo": repo_name,
                        "url": item.get("html_url"),
                        "comments": item.get("comments"),
                        "created_at": item.get("created_at"),
                        "body_snippet": (item.get("body") or "")[:300]
                    })
        except Exception as e:
            print(f"Lỗi khi quét query '{q}': {e}")
        time.sleep(1) # Tránh rate limit
        
    return bounties

def search_trending_data_needs():
    print("[2/3] Quét nhu cầu dữ liệu và micro-service có thể tự động hóa...")
    # Mô hình hóa các cơ hội dữ liệu công khai có giá trị thương mại
    data_opportunities = [
        {
            "type": "DATA_PRODUCT",
            "title": "Báo cáo dữ liệu: Top 500 Công cụ AI phát triển nhanh nhất 2026 (Kèm API & Pricing)",
            "monetization": "Đóng gói dataset JSON/CSV đưa lên HuggingFace / Gumroad / GitHub Sponsors",
            "cost": 0,
            "automation_level": "100% AI",
            "potential_revenue": "$20 - $100 / sale"
        },
        {
            "type": "FREE_MICRO_TOOL",
            "title": "VietQR Quick Link Generator API & Web Tool",
            "monetization": "Embed affiliate links (Hosting, Domain, SaaS) + BuyMeACoffee/VietQR",
            "cost": 0,
            "automation_level": "100% AI",
            "potential_revenue": "Thụ động từ traffic & donations"
        }
    ]
    return data_opportunities

def scan_all():
    bounties = search_github_bounties()
    data_ops = search_trending_data_needs()
    
    all_opportunities = {
        "last_scan": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_found": len(bounties) + len(data_ops),
        "code_bounties": bounties,
        "data_products": data_ops
    }
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_opportunities, f, ensure_ascii=False, indent=2)
        
    print(f"✅ Đã quét xong! Tìm thấy {all_opportunities['total_found']} cơ hội. Đã lưu vào {OUTPUT_FILE}")
    return all_opportunities

if __name__ == "__main__":
    scan_all()
