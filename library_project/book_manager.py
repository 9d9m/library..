from mongodb_connect import get_db
from pymongo import DESCENDING

db = get_db()
col = db["books"]

def add_book(book_data: dict):
    """新增单本图书 insert_one"""
    res = col.insert_one(book_data)
    print(f"✅ 新增图书成功，ID: {res.inserted_id}，影响文档：1")

def add_many_books(book_list: list):
    """批量新增图书 insert_many"""
    res = col.insert_many(book_list)
    print(f"✅ 批量新增成功，共插入 {len(res.inserted_ids)} 本")

def find_book_by_id(book_id):
    """单本查询 find_one"""
    ret = col.find_one({"_id": book_id})
    if ret is None:
        print("❌ 没有找到这本图书")
    return ret

def find_book_by_condition(cond: dict):
    """条件检索 find"""
    ret_list = list(col.find(cond))
    if len(ret_list) == 0:
        print("❌ 检索无结果")
    return ret_list

def update_book(cond: dict, new_data: dict):
    """修改单本 update_one"""
    res = col.update_one(cond, {"$set": new_data})
    print(f"✅ 修改完成，匹配：{res.matched_count}，修改：{res.modified_count}")

def delete_book(cond: dict):
    """删除单本 delete_one"""
    res = col.delete_one(cond)
    print(f"✅ 删除完成，已删除 {res.deleted_count} 条")

def delete_many_book(cond: dict):
    """批量删除 delete_many"""
    res = col.delete_many(cond)
    print(f"✅ 批量删除完成，已删除 {res.deleted_count} 条")

def get_book_rank_by_score():
    """评分排行，按分数降序"""
    ret = list(col.find({}).sort("score", DESCENDING))
    if len(ret) == 0:
        print("❌ 暂无图书数据")
    return ret
