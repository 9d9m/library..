from mongodb_connect import get_db
from datetime import datetime

db = get_db()
col = db["borrows"]

def borrow_register(borrow_data: dict):
    """借阅登记 insert_one"""
    res = col.insert_one(borrow_data)
    print(f"✅ 借阅登记成功，记录ID:{res.inserted_id}")

def return_book(borrow_id, return_time: datetime):
    """归还处理 update_many"""
    res = col.update_many(
        {"_id": borrow_id},
        {"$set": {"return_time": return_time, "status": "已归还"}}
    )
    print(f"✅ 归还处理，匹配：{res.matched_count}，更新：{res.modified_count}")

def find_overdue_borrow(deadline: datetime):
    """逾期查询：未归还 且 到期时间早于截止时间"""
    cond = {"due_time": {"$lt": deadline}, "status": "借阅中"}
    res_list = list(col.find(cond))
    if len(res_list) == 0:
        print("✅ 没有逾期记录")
    return res_list
