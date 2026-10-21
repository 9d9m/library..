from pymongo import MongoClient

# 统一连接参数
MONGO_HOST = "localhost"
MONGO_PORT = 27017
DB_NAME = "library_db"

client = None
db = None

def get_db():
    """获取数据库对象，单例连接"""
    global client, db
    if client is None or db is None:
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        db = client[DB_NAME]
    return db

def close_connection():
    """关闭连接，退出时调用"""
    global client
    if client is not None:
        client.close()
        print("\n✅ MongoDB连接已关闭")

def get_collection_count(col_name: str) -> int:
    """获取集合文档总数"""
    db = get_db()
    return db[col_name].count_documents({})
