"""
OPPORTUNITY ENGINE
Tiếp nhận dữ liệu từ Task Hunter, Lead Hunter và Trend Hunter.
Phân tích, chấm điểm và xếp hạng các cơ hội tạo ra doanh thu tốt nhất.
"""

import os
import sys
import json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def evaluate_opportunities(tasks, leads, trends):
    print("\n[OPPORTUNITY ENGINE] Đang tổng hợp và chấm điểm các cơ hội...")
    opportunities = []

    # 1. Evaluate Tasks (Jobs/Bounties)
    for t in tasks:
        score = 85
        if t.get("verified_escrow"):
            score += 10
        if t.get("status") in ["PENDING_MERGE", "CLAIM_SUBMITTED"]:
            score += 5  # Highest priority because work is already done and awaiting payout
        
        opportunities.append({
            "opp_id": f"OPP_{t['id']}",
            "source_type": "TASK",
            "title": t["title"],
            "target": t.get("source"),
            "expected_payout": t.get("reward"),
            "score": score,
            "speed": "FAST (< 24-48h)",
            "capital_required": 0,
            "raw_data": t
        })

    # 2. Evaluate Leads (Clients)
    for l in leads:
        score = 80
        if l.get("city") in ["Hà Nội", "TP.HCM"]:
            score += 5
        if l.get("willingness_to_pay") in ["Cao", "Rất cao"]:
            score += 10
        
        opportunities.append({
            "opp_id": f"OPP_{l['id']}",
            "source_type": "CLIENT",
            "title": f"B2B Web & VietQR cho {l['name']}",
            "target": l["name"],
            "expected_payout": f"{l['target_deal_size']:,} VNĐ",
            "score": score,
            "speed": "DIRECT OUTREACH",
            "capital_required": 0,
            "raw_data": l
        })

    # 3. Evaluate Trends (Products)
    for tr in trends:
        score = 75
        opportunities.append({
            "opp_id": f"OPP_{tr['id']}",
            "source_type": "PRODUCT",
            "title": tr["title"],
            "target": tr["target_audience"],
            "expected_payout": tr["monetization_model"],
            "score": score,
            "speed": "PASSIVE REVENUE STREAM",
            "capital_required": 0,
            "raw_data": tr
        })

    # Sort descending by score
    opportunities.sort(key=lambda x: x["score"], reverse=True)
    print(f"  -> Opportunity Engine đã xếp hạng {len(opportunities)} cơ hội. Top cơ hội điểm cao nhất: {opportunities[0]['title']} ({opportunities[0]['score']} pts)")
    return opportunities

if __name__ == "__main__":
    from task_hunter import hunt_tasks
    from lead_hunter import hunt_leads
    from trend_hunter import hunt_trends
    opps = evaluate_opportunities(hunt_tasks(), hunt_leads(), hunt_trends())
    print(json.dumps(opps[:3], ensure_ascii=False, indent=2))
