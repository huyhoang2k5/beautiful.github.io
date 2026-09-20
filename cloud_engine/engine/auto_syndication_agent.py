"""
AUTO SYNDICATION AGENT
Tự động hóa đa nền tảng (Việt Nam & Quốc Tế) để khai thác triệt để:
1. International Bounties (Jobs for AI Agents, RustChain, MergeEarn, Omi)
2. B2B Outbound Funnel (12 Leads cà phê, homestay, spa)
3. Social Syndication Queue (Reddit, Twitter/X, Threads, Facebook Groups)
4. Free Lead Magnet Tool (VietQR Generator)
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import subprocess
from datetime import datetime

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ENGINE_DIR = os.path.dirname(CURRENT_DIR)
DISTRIBUTION_DIR = os.path.join(ENGINE_DIR, "distribution")
os.makedirs(DISTRIBUTION_DIR, exist_ok=True)

def generate_multi_platform_broadcast():
    print("[AUTO SYNDICATION] Đang tổng hợp và tự động hóa các kênh quảng bá & kiếm tiền...")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. International Channels Broadcast
    reddit_post = {
        "platform": "Reddit (r/SideProject, r/webdev)",
        "target": "Global Developers & Indie Hackers",
        "title": "I built a lightweight 0-dependency QR Payment Widget for web apps (100% Free & Open Source)",
        "link": "https://github.com/huyhoang2k5/vietqr-widget",
        "demo": "https://huyhoang2k5.github.io/vietqr-widget/"
    }
    
    twitter_thread = {
        "platform": "Twitter / X",
        "target": "Tech Twitter & Solopreneurs",
        "hook": "How to build & monetize an open-source tool with $0 server cost in 2026: 🧵👇",
        "link": "https://huyhoang2k5.github.io/vietqr-widget/"
    }
    
    # 2. Domestic Channels Broadcast
    fb_groups = [
        {
            "group": "Hội Chủ Quán Cafe, Trà Sữa & Nhà Hàng Toàn Quốc",
            "topic": "Menu Điện Tử & VietQR Tại Bàn",
            "hook": "Tặng các chủ quán bộ mẫu Menu Điện Tử VietQR tại bàn không mất phí sàn",
            "cta_link": "https://huyhoang2k5.github.io/solopreneur-kit/blog/huong-dan-tao-menu-dien-tu-vietqr.html"
        },
        {
            "group": "Cộng Đồng Homestay & Du Lịch Tự Túc",
            "topic": "Giải Pháp Nhận Cọc Giữ Phòng Tự Động",
            "hook": "Cách homestay nhận cọc 200k tự động tránh bùng phòng & né phí 15% của OTA",
            "cta_link": "https://huyhoang2k5.github.io/solopreneur-kit/blog/giai-phap-nhan-coc-phong-homestay-tu-dong.html"
        },
        {
            "group": "Cộng Đồng Người Bán Hàng Online & Freelancer",
            "topic": "Công Cụ Tạo Mã VietQR Miễn Phí",
            "hook": "Công cụ tạo mã QR chuyển khoản Napas247 miễn phí, tải ảnh PNG trong 3 giây",
            "cta_link": "https://huyhoang2k5.github.io/solopreneur-kit/tools/vietqr-generator/"
        }
    ]

    broadcast_manifest = {
        "generated_at": timestamp,
        "international": [reddit_post, twitter_thread],
        "domestic": fb_groups,
        "active_bounties_summary": {
            "base_usdc": "3 tasks ($27.00 USDC) on Jobs for AI Agents",
            "nimiq": "20 NIM on MergeEarn PR #45",
            "rustchain": "8.1 RTC on RustChain Bounties",
            "b2b_pipeline": "12 leads (2.888.000 VNĐ) on Solopreneur Kit"
        }
    }

    manifest_file = os.path.join(DISTRIBUTION_DIR, "live_broadcast_manifest.json")
    with open(manifest_file, "w", encoding="utf-8") as f:
        json.dump(broadcast_manifest, f, ensure_ascii=False, indent=2)
        
    print(f"  -> Đã cập nhật bản phân phối đa kênh tại: {manifest_file}")
    return broadcast_manifest

if __name__ == "__main__":
    generate_multi_platform_broadcast()
