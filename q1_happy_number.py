def is_happy_number(n: int) -> bool:
    def sum_of_squares(num: int) -> int:
        # محاسبه مجموع توان دو ارقام عدد
        return sum(int(digit) ** 2 for digit in str(num))

    seen = set()  # مجموعه‌ای برای ردیابی اعداد مشاهده‌شده
    iterations = 0  # شمارنده تکرارها
    
    while n != 1 and n not in seen and iterations < 200:
        seen.add(n)
        n = sum_of_squares(n)
        iterations += 1

    return n == 1  # اگر عدد نهایی برابر 1 باشد، عدد خوشحال است

# ورودی از کاربر
try:
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Input must be a positive integer!")
    else:
        if is_happy_number(n):
            print("Happy")
        else:
            print("Not Happy")
except ValueError:
    print("Invalid input! Please enter an integer.")