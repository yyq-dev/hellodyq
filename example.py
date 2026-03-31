#!/usr/bin/python3
# 今天是3月31日，还剩23天

import json
import os
from datetime import datetime

# 账单文件名称（数据存在这里）
BILL_FILE = "my_bills.json"

# 初始化账单数据
def init_bills():
    # 如果文件不存在，创建空文件
    if not os.path.exists(BILL_FILE):
        with open(BILL_FILE, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)

# 加载账单
def load_bills():
    with open(BILL_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# 保存账单
def save_bills(bills):
    with open(BILL_FILE, "w", encoding="utf-8") as f:
        json.dump(bills, f, ensure_ascii=False, indent=4)

# 添加一笔账单
def add_bill():
    print("\n--- 新增账单 ---")
    type_ = input("请输入类型（收入/支出）：").strip()
    while type_ not in ["收入", "支出"]:
        type_ = input("输入错误！只能是 收入/支出：").strip()

    money = input("请输入金额（数字）：")
    while not money.replace(".", "").isdigit():
        money = input("输入错误！请输入数字：")
    money = float(money)

    remark = input("请输入备注（如：吃饭、工资）：").strip()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    bill = {
        "time": now,
        "type": type_,
        "money": money,
        "remark": remark
    }

    bills = load_bills()
    bills.append(bill)
    save_bills(bills)
    print(f"✅ 记账成功！{now} - {type_} {money}元 - {remark}")

# 查看所有账单
def show_bills():
    bills = load_bills()
    if not bills:
        print("\n📭 暂无账单记录")
        return

    print("\n--- 所有账单 ---")
    for i, bill in enumerate(bills, 1):
        print(f"{i}. {bill['time']} | {bill['type']} | {bill['money']}元 | {bill['remark']}")

# 统计账单
def count_bills():
    bills = load_bills()
    if not bills:
        print("\n📭 暂无账单记录")
        return

    income = 0.0
    outcome = 0.0
    for b in bills:
        if b["type"] == "收入":
            income += b["money"]
        else:
            outcome += b["money"]

    print("\n--- 账单统计 ---")
    print(f"💰 总收入：{income:.2f} 元")
    print(f"💸 总支出：{outcome:.2f} 元")
    print(f"📊 当前结余：{income - outcome:.2f} 元")

# 主菜单
def main():
    init_bills()
    print("=" * 30)
    print("    📒 个人记账工具")
    print("=" * 30)

    while True:
        print("\n===== 菜单 =====")
        print("1. 记一笔账")
        print("2. 查看所有账单")
        print("3. 统计收支")
        print("0. 退出程序")
        choice = input("请输入选项（0-3）：").strip()

        if choice == "1":
            add_bill()
        elif choice == "2":
            show_bills()
        elif choice == "3":
            count_bills()
        elif choice == "0":
            print("\n👋 感谢使用，再见！")
            break
        else:
            print("❌ 输入错误，请重新选择")

if __name__ == "__main__":
    main()
