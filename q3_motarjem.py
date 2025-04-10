# ساخت دیکشنری از ورودی
n = int(input("Enter number of dictionary entries: "))
my_dict = {}
for _ in range(n):
    eng, fa = input().split()
    my_dict[eng] = fa

my_str = input("Enter your text: ")
chek_list = my_str.split()

# استفاده از join برای ترکیب کلمات
translated_words = [my_dict.get(word, word) for word in chek_list]

# چاپ جمله ترجمه شده
print(" ".join(translated_words))