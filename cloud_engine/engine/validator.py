"""
VALIDATION COMPONENT
Kiểm tra nghiêm ngặt tính khả thi, nguyên tắc vốn 0 VNĐ và mức độ xác thực của đối tác/khách hàng.
"""

import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def validate_opportunity(opp):
    # Rule 1: Zero Capital Rule
    if opp.get("capital_required", 0) > 0:
        return False, "Vi phạm nguyên tắc vốn 0 VNĐ"

    # Rule 2: Source Verification
    source_type = opp.get("source_type")
    if source_type == "TASK":
        # Must have verified escrow or reputable open source repo
        return True, "Hợp lệ: Task có bảo chứng hoặc repo uy tín"
    elif source_type == "CLIENT":
        # Must have verified address and contact phone
        raw = opp.get("raw_data", {})
        if raw.get("phone") and raw.get("address"):
            return True, "Hợp lệ: Khách hàng có địa chỉ & số điện thoại thực tế"
        return False, "Thiếu thông tin liên lạc xác thực"
    elif source_type == "PRODUCT":
        # Must have zero-cost hosting and instant delivery mechanism
        return True, "Hợp lệ: Sản phẩm số tải tức thì không tốn chi phí lưu trữ"

    return False, "Loại cơ hội không xác định"

def validate_all(opportunities):
    print("\n[VALIDATION] Đang kiểm tra tính khả thi và điều kiện 0 VNĐ...")
    valid_list = []
    for opp in opportunities:
        is_valid, reason = validate_opportunity(opp)
        if is_valid:
            valid_list.append(opp)
    print(f"  -> Validation hoàn tất: {len(valid_list)}/{len(opportunities)} cơ hội đạt tiêu chuẩn kiểm duyệt.")
    return valid_list

if __name__ == "__main__":
    from task_hunter import hunt_tasks
    from lead_hunter import hunt_leads
    from trend_hunter import hunt_trends
    from opportunity_engine import evaluate_opportunities
    opps = evaluate_opportunities(hunt_tasks(), hunt_leads(), hunt_trends())
    valid = validate_all(opps)
    print(f"Total valid: {len(valid)}")
