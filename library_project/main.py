from mongodb_connect import get_db, close_connection, get_collection_count
import book_manager
import reader_manager
import borrow_manager
import stat_manager
from datetime import datetime

def show_menu():
    print("\n===== 📖 图书管理系统 主菜单 =====")
    print("1. 添加图书")
    print("2. 条件检索图书")
    print("3. 修改图书信息")
    print("4. 删除图书")
    print("5. 读者管理 & 等级分布统计")
    print("6. 借阅登记 / 归还处理 / 逾期查询")
    print("7. 聚合统计（分类/借阅趋势/畅销榜）")
    print("8. 图书评分排行")
    print("0. 退出系统")
    print("==================================")

def main():
    # 启动打印连接状态 + 各集合总数
    print("🔌 正在连接MongoDB...")
    db = get_db()
    print("✅ 数据库连接成功！")
    print(f"📚 books集合总数：{get_collection_count('books')}")
    print(f"👤 readers集合总数：{get_collection_count('readers')}")
    print(f"📝 borrows集合总数：{get_collection_count('borrows')}")

    while True:
        show_menu()
        opt = input("请输入功能编号：")
        if opt == "1":
            name = input("图书名称：")
            category = input("图书分类：")
            price = float(input("价格："))
            stock = int(input("库存："))
            score = float(input("评分："))
            data = {"name": name, "category": category, "price": price, "stock": stock, "score": score}
            book_manager.add_book(data)

        elif opt == "2":
            key = input("检索字段(name/category)：")
            val = input("检索值：")
            res = book_manager.find_book_by_condition({key: val})
if __name__ == "__main__":
    main()
