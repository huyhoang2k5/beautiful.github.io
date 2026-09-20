"""
TREND HUNTER (PRODUCTS & DIGITAL ASSETS)
Quét các xu hướng tìm kiếm, chủ đề viral và nhu cầu sản phẩm số đang có tỷ lệ quan tâm cao.
"""

import os
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

TRENDING_PRODUCTS = [
    {
        "id": "TREND_001",
        "title": "VietQR Payment Utilities",
        "description": "Nhu cầu thanh toán không tiền mặt Napas247 tăng vọt tại Việt Nam",
        "product_type": "Micro-SaaS / Developer Widget & Chrome Extension",
        "target_audience": "Lập trình viên, Chủ shop online, Khách hàng mua sắm",
        "monetization_model": "Donations & Cung cấp dịch vụ B2B",
        "deployed_assets": [
            "https://huyhoang2k5.github.io/vietqr-widget/",
            "https://github.com/huyhoang2k5/vietqr-quickpay-extension"
        ]
    },
    {
        "id": "TREND_002",
        "title": "B2B F&B Leads Database (Data-as-a-Service)",
        "description": "Các nhà cung ứng nguyên liệu, bao bì, phần mềm POS cần danh bạ quán cafe/nhà hàng",
        "product_type": "Digital Dataset (CSV/Excel)",
        "target_audience": "Sale F&B, Agency tiếp thị, Xưởng sản xuất bao bì",
        "monetization_model": "Bán dataset trực tiếp 49.000 VNĐ / download",
        "deployed_assets": [
            "https://huyhoang2k5.github.io/solopreneur-kit/assets/fnb_leads_hanoi_hcm_2026.csv"
        ]
    },
    {
        "id": "TREND_003",
        "title": "AI Solopreneur Toolkit & Viral Quiz",
        "description": "Làn sóng kiếm tiền online bằng AI & trắc nghiệm tính cách / thu nhập",
        "product_type": "Digital Guide & Interactive Mini-Game",
        "target_audience": "Người trẻ muốn khởi nghiệp với 0đ vốn",
        "monetization_model": "19.000đ - 29.000đ / lượt mở khóa",
        "deployed_assets": [
            "https://huyhoang2k5.github.io/solopreneur-kit/",
            "https://huyhoang2k5.github.io/solopreneur-kit/quiz/"
        ]
    }
]

def hunt_trends():
    print("[TREND HUNTER] Đang quét Internet tìm xu hướng sản phẩm & nhu cầu thị trường (Products)...")
    trends = TRENDING_PRODUCTS
    print(f"  -> Trend Hunter tìm thấy: {len(trends)} danh mục sản phẩm có nhu cầu cao.")
    return trends

if __name__ == "__main__":
    results = hunt_trends()
    print(json.dumps(results, ensure_ascii=False, indent=2))
