"""
AUTONOMOUS MONEY-SEEKING AGENT - EVALUATOR MODULE
Đánh giá và xếp hạng các cơ hội kiếm tiền dựa trên:
1. Tính khả thi để AI tự thực hiện 100% (Feasibility)
2. Giá trị tiền thưởng/doanh thu (Reward)
3. Mức độ cạnh tranh (Competition)
4. Rủi ro và chi phí (Bắt buộc Vốn = 0)
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DISCOVERED_FILE = os.path.join(BASE_DIR, "discovered_opportunities.json")
EVALUATED_FILE = os.path.join(BASE_DIR, "evaluated_opportunities.json")

def evaluate_opportunities():
    if not os.path.exists(DISCOVERED_FILE):
        print("Chưa có dữ liệu scan.")
        return []

    with open(DISCOVERED_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    bounties = data.get("code_bounties", [])
    data_products = data.get("data_products", [])
    
    scored_items = []

    # Đánh giá các Code Bounties
    for b in bounties:
        title = b.get("title", "").lower()
        comments = b.get("comments", 0)
        
        # Tiêu chí:
        # - Cạnh tranh thấp (comments < 3): +3 điểm
        # - Yêu cầu rõ ràng (frontend/accessibility/copy/fix/label): +4 điểm
        # - Vốn bắt buộc = 0: Đạt
        score = 5.0
        if comments == 0:
            score += 3.0
        elif comments <= 2:
            score += 1.5
        else:
            score -= 2.0

        if any(k in title for k in ["accessibility", "label", "copy", "compact", "add", "fix", "improve"]):
            score += 2.0
            
        scored_items.append({
            "type": b.get("type"),
            "title": b.get("title"),
            "url": b.get("url"),
            "repo": b.get("repo"),
            "comments": comments,
            "score": round(score, 2),
            "status": "READY_FOR_EXECUTION"
        })

    # Sắp xếp theo điểm số cao nhất
    scored_items.sort(key=lambda x: x["score"], reverse=True)

    result = {
        "evaluated_at": data.get("last_scan"),
        "top_opportunities": scored_items[:5]
    }

    with open(EVALUATED_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✅ Đã đánh giá xong! Top 1 cơ hội: {scored_items[0]['title']} (Điểm: {scored_items[0]['score']})")
    return scored_items

if __name__ == "__main__":
    evaluate_opportunities()
