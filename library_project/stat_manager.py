from mongodb_connect import get_db

db = get_db()
book_col = db["books"]
borrow_col = db["borrows"]

def stat_book_by_category():
    """分类统计：分组，库存总量、平均价格、图书数量，库存降序"""
    pipeline = [
        {
            "$group": {
                "_id": "$category",
                "total_stock": {"$sum": "$stock"},
                "avg_price": {"$avg": "$price"},
                "book_count": {"$sum": 1}
            }
        },
        {"$sort": {"total_stock": -1}}
    ]
    result = list(book_col.aggregate(pipeline))
    if not result:
        print("❌ 无图书统计数据")
    return result

def stat_borrow_trend_by_year():
    """借阅趋势：按年份分组统计借阅量"""
    pipeline = [
        {
            "$group": {
                "_id": {"$year": "$borrow_time"},
                "borrow_count": {"$sum": 1}
            }
        },
        {"$sort": {"_id": 1}}
    ]
    raw = list(borrow_col.aggregate(pipeline))
    # 格式化输出
    out = []
    for item in raw:
        year = item["_id"]
        if year is None:
            continue
        out.append({"year": year, "count": item["borrow_count"]})
    if len(out) == 0:
        print("❌ 暂无借阅趋势数据")
    return out

def stat_hot_book_topN(n: int = 3):
    """畅销榜：按借阅次数取最多的图书"""
    pipeline = [
        {"$group": {"_id": "$book_id", "borrow_times": {"$sum": 1}}},
        {"$sort": {"borrow_times": -1}},
        {"$limit": n}
    ]
    res = list(borrow_col.aggregate(pipeline))
    if len(res) == 0:
        print("❌ 暂无借阅记录，无法生成畅销榜")
    return res
