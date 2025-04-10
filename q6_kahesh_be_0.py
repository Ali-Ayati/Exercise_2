num = int(input("Enter your number = "))
steps = 0  # شمارنده تعداد گام‌ها

while num != 0:
    if num % 2 == 0:  # اگر عدد زوج باشد
        num = num // 2  # تقسیم عدد بر 2
    else:  # اگر عدد فرد باشد
        num -= 1  # کاهش 1 از عدد
    steps += 1  # افزایش تعداد گام‌ها

print(steps)