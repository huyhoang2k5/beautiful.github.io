"""
CUSTOMER ACQUISITION AGENT
Tự động hóa 100% quy trình tìm kiếm khách hàng, tạo demo cá nhân hóa, 
tạo nội dung quảng bá đa kênh và tạo đường link tiếp cận trực tiếp.
"""

import os
import sys
import json
import urllib.parse
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ENGINE_DIR = os.path.dirname(CURRENT_DIR)
LANDING_PAGE_DIR = os.path.join(ENGINE_DIR, "landing_page")

# Extended database of high-intent B2B leads across Vietnam
EXPANDED_LEADS = [
    {
        "id": "LEAD_001",
        "name": "Chill 'n Feel Coffee",
        "category": "Cafe",
        "city": "Hà Nội",
        "address": "50 Trương Công Giai, Cầu Giấy",
        "phone": "0848889292",
        "need": "Website Menu Điện Tử & VietQR",
        "target_deal_size": 199000,
        "slug": "chill-n-feel"
    },
    {
        "id": "LEAD_002",
        "name": "ULA Cafe & Fast Food 24/7",
        "category": "Cafe & Ăn Vặt",
        "city": "Hà Nội",
        "address": "81 Nguyễn Khang, Cầu Giấy",
        "phone": "0865163588",
        "need": "Website Menu Đặt Món Đêm & VietQR",
        "target_deal_size": 199000,
        "slug": "ula-cafe"
    },
    {
        "id": "LEAD_003",
        "name": "Nuwa Coffee",
        "category": "Cafe",
        "city": "Hà Nội",
        "address": "A10-CT1 KĐT Nam Trung Yên, Cầu Giấy",
        "phone": "0978613983",
        "need": "Menu QR & Thanh toán bàn",
        "target_deal_size": 199000,
        "slug": "nuwa-coffee"
    },
    {
        "id": "LEAD_004",
        "name": "Coming Home Cafe",
        "category": "Specialty Coffee",
        "city": "TP.HCM",
        "address": "Lầu 1, 158/17 Nguyễn Công Trứ, Quận 1",
        "phone": "0981789607",
        "need": "Trang giới thiệu quán & Menu VietQR",
        "target_deal_size": 299000,
        "slug": "coming-home"
    },
    {
        "id": "LEAD_005",
        "name": "Trulli Café",
        "category": "Cafe Ý & Bánh",
        "city": "TP.HCM",
        "address": "24-26 Phạm Ngọc Thạch, Quận 3",
        "phone": "0908356669",
        "need": "Menu bánh & Đặt bàn trước",
        "target_deal_size": 299000,
        "slug": "trulli-cafe"
    },
    {
        "id": "LEAD_006",
        "name": "Daisy Cafe Đà Nẵng",
        "category": "Cafe",
        "city": "Đà Nẵng",
        "address": "31/5 Lê Hồng Phong, Hải Châu",
        "phone": "0905525755",
        "need": "Website Menu Đặt Món & VietQR",
        "target_deal_size": 199000,
        "slug": "daisy-cafe"
    },
    {
        "id": "LEAD_007",
        "name": "Fil's Cafe Đà Nẵng",
        "category": "Specialty Coffee",
        "city": "Đà Nẵng",
        "address": "K225/3 Đống Đa, Hải Châu",
        "phone": "0905888136",
        "need": "Menu Cold Brew & Đặt Bàn",
        "target_deal_size": 199000,
        "slug": "fils-cafe"
    },
    {
        "id": "LEAD_008",
        "name": "Nắng Homestay Đà Lạt",
        "category": "Homestay & Du Lịch",
        "city": "Đà Lạt",
        "address": "Đường Lâm Sinh, Phường 5, TP. Đà Lạt",
        "phone": "0385593364",
        "need": "Web Đặt Phòng & Nhận Cọc VietQR Tự Động",
        "target_deal_size": 299000,
        "slug": "nang-homestay"
    },
    {
        "id": "LEAD_009",
        "name": "Mây Homestay Đà Lạt",
        "category": "Homestay",
        "city": "Đà Lạt",
        "address": "77 Hoàng Hoa Thám, Phường 10, Đà Lạt",
        "phone": "0933221100",
        "need": "Web Đặt Phòng Trực Tiếp Giữ Cọc 200k",
        "target_deal_size": 299000,
        "slug": "may-homestay"
    },
    {
        "id": "LEAD_010",
        "name": "Củi Homestay Đà Lạt",
        "category": "Homestay",
        "city": "Đà Lạt",
        "address": "79 Triệu Việt Vương, Phường 4, Đà Lạt",
        "phone": "0911668844",
        "need": "Web Đặt Phòng & Tránh Phí Sàn OTA 15%",
        "target_deal_size": 299000,
        "slug": "cui-homestay"
    },
    {
        "id": "LEAD_011",
        "name": "Lala Nail & Beauty Spa",
        "category": "Nail & Spa",
        "city": "Hà Nội",
        "address": "120 Nguyễn Thái Học, Ba Đình",
        "phone": "0912345678",
        "need": "Trang Đặt Lịch Làm Móng & Cọc Giữ Chỗ",
        "target_deal_size": 199000,
        "slug": "lala-nail-spa"
    },
    {
        "id": "LEAD_012",
        "name": "Zen Spa & Wellness",
        "category": "Spa & Massage",
        "city": "TP.HCM",
        "address": "45 Lê Lợi, Bến Nghé, Quận 1",
        "phone": "0903123456",
        "need": "Trang Đặt Liệu Trình & Thanh Toán VietQR",
        "target_deal_size": 299000,
        "slug": "zen-spa"
    }
]

def generate_personalized_demo_if_missing(lead):
    slug = lead.get("slug")
    demo_dir = os.path.join(LANDING_PAGE_DIR, "demos", slug)
    demo_file = os.path.join(demo_dir, "index.html")
    
    if os.path.exists(demo_file):
        return f"https://huyhoang2k5.github.io/solopreneur-kit/demos/{slug}/"
    
    os.makedirs(demo_dir, exist_ok=True)
    
    is_homestay = "Homestay" in lead["category"]
    is_spa = "Nail" in lead["category"] or "Spa" in lead["category"]
    
    if is_homestay:
        title = f"{lead['name']} - Đặt Phòng Trực Tiếp Nhận Ưu Đãi 10%"
        headline = f"Nghỉ Dưỡng Thảnh Thơi Tại {lead['name']}"
        desc = f"Chào mừng bạn đến với {lead['name']} ({lead['address']}). Đặt phòng trực tiếp không qua trung gian, nhận xác nhận giữ phòng tức thì qua VietQR."
        action_btn = "⚡ Đặt Phòng & Nhận Xác Nhận Tức Thì"
        price_tag = "Giá phòng từ: 450.000đ/đêm"
    elif is_spa:
        title = f"{lead['name']} - Đặt Lịch Làm Đẹp & Thư Giãn"
        headline = f"Trải Nghiệm Dịch Vụ Cao Cấp Tại {lead['name']}"
        desc = f"Địa chỉ: {lead['address']}. Đặt lịch hẹn trước để không phải chờ đợi, giữ chỗ chỉ với 50.000đ cọc qua VietQR."
        action_btn = "💅 Đặt Lịch Hẹn Ngay"
        price_tag = "Dịch vụ từ: 120.000đ"
    else:
        title = f"{lead['name']} - Menu Điện Tử & Thanh Toán Bàn"
        headline = f"Thưởng Thức Trọn Vẹn Tại {lead['name']}"
        desc = f"Địa chỉ: {lead['address']}. Xem menu điện tử và gọi món thanh toán nhanh không cần tiền mặt qua mã VietQR."
        action_btn = "☕ Xem Menu & Đặt Món"
        price_tag = "Đồ uống từ: 35.000đ"

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', sans-serif; }}
    body {{ background: #0b0f19; color: #f8fafc; line-height: 1.6; padding: 2rem 1rem; }}
    .container {{ max-width: 600px; margin: 0 auto; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 1.5rem; padding: 2rem; backdrop-filter: blur(10px); }}
    .badge {{ display: inline-block; padding: 0.35rem 0.85rem; border-radius: 9999px; background: rgba(16, 185, 129, 0.15); color: #34d399; font-size: 0.85rem; font-weight: 600; margin-bottom: 1rem; }}
    h1 {{ font-size: 1.8rem; font-weight: 800; margin-bottom: 0.75rem; color: #fff; }}
    p.desc {{ color: #94a3b8; font-size: 0.95rem; margin-bottom: 1.5rem; }}
    .info-card {{ background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255,255,255,0.06); border-radius: 1rem; padding: 1.25rem; margin-bottom: 1.5rem; }}
    .info-item {{ display: flex; justify-content: space-between; margin-bottom: 0.5rem; font-size: 0.9rem; }}
    .info-label {{ color: #94a3b8; }}
    .info-val {{ color: #fff; font-weight: 600; }}
    .qr-box {{ text-align: center; background: #fff; border-radius: 1rem; padding: 1.25rem; margin-bottom: 1.5rem; }}
    .qr-box img {{ width: 200px; height: 200px; object-fit: contain; }}
    .btn {{ display: block; width: 100%; text-align: center; padding: 0.9rem; border-radius: 0.75rem; font-weight: 700; text-decoration: none; font-size: 1rem; }}
    .btn-primary {{ background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); color: #fff; margin-bottom: 0.75rem; }}
    .btn-zalo {{ background: #0068ff; color: #fff; }}
    .footer-note {{ text-align: center; font-size: 0.8rem; color: #64748b; margin-top: 1.5rem; }}
  </style>
</head>
<body>
  <div class="container">
    <div class="badge">✨ BẢN DEMO THỰC TẾ DÀNH RIÊNG CHO {lead['name'].upper()}</div>
    <h1>{headline}</h1>
    <p class="desc">{desc}</p>

    <div class="info-card">
      <div class="info-item"><span class="info-label">Cơ sở:</span><span class="info-val">{lead['name']}</span></div>
      <div class="info-item"><span class="info-label">Địa chỉ:</span><span class="info-val">{lead['address']}</span></div>
      <div class="info-item"><span class="info-label">Hotline:</span><span class="info-val">{lead['phone']}</span></div>
      <div class="info-item"><span class="info-label">Mức giá:</span><span class="info-val" style="color: #34d399;">{price_tag}</span></div>
    </div>

    <div class="qr-box">
      <img src="https://img.vietqr.io/image/TPB-20058999999-compact2.png?amount={lead['target_deal_size']}&addInfo={lead['slug'].upper()}%20THANHTOAN" alt="VietQR Demo">
      <p style="color: #1e293b; font-size: 0.85rem; font-weight: 600; margin-top: 0.5rem;">Quét QR thanh toán tự động không phí sàn</p>
    </div>

    <a href="https://zalo.me/{lead['phone']}" class="btn btn-primary">{action_btn}</a>
    <a href="https://zalo.me/{lead['phone']}" class="btn btn-zalo">💬 Liên Hệ Trực Tiếp Qua Zalo ({lead['phone']})</a>

    <div class="footer-note">
      Trang web mẫu được xây dựng tự động bởi Solopreneur AI Toolkit.<br>
      Kích hoạt chính thức cho cơ sở chỉ từ 199.000 VNĐ.
    </div>
  </div>
</body>
</html>
"""
    with open(demo_file, "w", encoding="utf-8") as f:
        f.write(html)
    
    return f"https://huyhoang2k5.github.io/solopreneur-kit/demos/{slug}/"

def build_customer_acquisition_pack():
    print("[CUSTOMER ACQUISITION] Bắt đầu khởi tạo hệ thống tiếp cận khách hàng tự động...")
    
    outreach_batch = []
    
    for lead in EXPANDED_LEADS:
        demo_url = generate_personalized_demo_if_missing(lead)
        
        # Pitch formulation
        if "Homestay" in lead["category"]:
            pitch = (
                f"Chào anh/chị quản lý {lead['name']},\n\n"
                f"Em thấy homestay mình bên {lead['address']} rất đẹp nhưng hiện tại khách đặt qua OTA hay bị cắn phí 15-20% và dễ bị bùng cọc.\n"
                f"Em vừa làm sẵn 1 trang web đặt phòng & nhận cọc VietQR tự động riêng cho {lead['name']}: {demo_url}\n\n"
                f"Khách quét mã chuyển cọc là tiền về thẳng tài khoản, tự động báo tin nhắn xác nhận. Anh/chị xem thử nhé!"
            )
        elif "Nail" in lead["category"] or "Spa" in lead["category"]:
            pitch = (
                f"Chào {lead['name']},\n\n"
                f"Em thấy spa mình bên {lead['address']} khách đặt lịch hay bị trùng giờ hoặc quên hẹn.\n"
                f"Em vừa thiết kế sẵn 1 trang đặt lịch hẹn & nhận cọc giữ chỗ VietQR riêng cho quán: {demo_url}\n\n"
                f"Khách chọn dịch vụ và chuyển cọc 50k là tự động chốt lịch. Anh/chị bấm vào xem thử giao diện nhé!"
            )
        else:
            pitch = (
                f"Chào anh/chị quản lý {lead['name']},\n\n"
                f"Em thấy quán mình ở {lead['address']} rất đông khách vào giờ cao điểm.\n"
                f"Em vừa dựng sẵn cho quán 1 trang Menu Điện Tử & Gọi Món VietQR tại bàn: {demo_url}\n\n"
                f"Khách chỉ cần quét mã trên bàn là gọi món & thanh toán thẳng về tài khoản quán, không cần nhân viên đứng ghi chép. Anh/chị xem thử demo nhé!"
            )

        encoded_pitch = urllib.parse.quote(pitch)
        zalo_link = f"https://zalo.me/{lead['phone']}?text={encoded_pitch}"
        
        outreach_batch.append({
            "id": lead["id"],
            "name": lead["name"],
            "category": lead["category"],
            "phone": lead["phone"],
            "city": lead["city"],
            "demo_url": demo_url,
            "zalo_link": zalo_link,
            "pitch": pitch,
            "target_deal_size": lead["target_deal_size"]
        })

    # Save to outreach batch file
    outreach_dir = os.path.join(ENGINE_DIR, "b2b_outreach")
    os.makedirs(outreach_dir, exist_ok=True)
    outreach_file = os.path.join(outreach_dir, "active_outreach_batch.json")
    with open(outreach_file, "w", encoding="utf-8") as f:
        json.dump(outreach_batch, f, ensure_ascii=False, indent=2)
        
    print(f"  -> Đã tạo gói tiếp cận khách hàng cho {len(outreach_batch)} cơ sở kinh doanh.")
    print(f"  -> Dữ liệu đã lưu tại: {outreach_file}")
    
    return outreach_batch

if __name__ == "__main__":
    batch = build_customer_acquisition_pack()
    print(f"Hoàn thành {len(batch)} leads.")
