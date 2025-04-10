def normalize(data):
    min_val = min(data)
    max_val = max(data)
    
    # جلوگیری از تقسیم بر صفر
    if max_val == min_val:
        return [0 for _ in data]
    
    normalized = [(x - min_val) / (max_val - min_val) for x in data]
    return [round(val, 3) for val in normalized]  # گرد کردن به 3 رقم اعشار

# تست با نمونه سوال
# data = [12, 19, 23, 25]
# print(normalize(data))  # خروجی: [0.0, 0.538, 0.846, 1.0]

# دریافت ورودی از کاربر:
data = list(map(int, input("Enter your numbers (space-separated): ").split()))
print(normalize(data))