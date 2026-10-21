from mongodb_connect import get_db

db = get_db()
col = db["readers"]

def add_reader(reader_data: dict):
    res = col.insert_one(reader_data)
    print(f"✅ 新增读者成功，ID:{res.inserted_id}，影响文档：1")

def find_reader(cond: dict):
    res_list = list(col.find(cond))
    if len(res_list) == 0:
        print("❌ 未查询到读者信息")
    return res_list

def count_reader(cond: dict = {}):
    """统计读者数量 count_documents"""
    cnt = col.count_documents(cond)
    print(f"📊 满足条件读者数量：{cnt}")
    return cnt

def get_distinct_college():
    """distinct：获取所有学院名称"""
    colleges = col.distinct("college")
    print(f"📚 全部学院列表：{colleges}")
    return colleges

def get_level_distribution():
    """读者等级分布聚合"""
    pipeline = [
        {"$group": {"_id": "$level", "count": {"$sum": 1}}}
    ]
    res = list(col.aggregate(pipeline))
    return res
