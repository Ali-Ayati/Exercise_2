# Exercise 2

This directory contains **7 Python exercises** focused on basic programming concepts such as:
- String manipulation
- Dictionaries
- Functions
- Loops
- Conditional statements

Each exercise is saved in a separate file in the format: `q<number>_<task-name>.py`

---

## Problem Descriptions

### 🔹 Question 1 – q1_happy_number.py _ عدد خوشحال
*Description:*  

برنامه ای بنویسید که بررسی کند که آیا عدد صحیح داده شده در ورودی عددی خوشحال است یا خیر. در صورت خوشحال بودن خروجی برابر با True و درغیر اینصورت برابر با False باشد.

عدد خوشحال: عدد خوشحال عددی است که با استفاده از پروسه زیر تعریف می شود:

• عدد صحیح مثبت داده شده در ورودی را با مجموع توان دو ارقام آن جایگزین نمایید.

• پروسه فوق را تا زمانی تکرار کنید که تنها یک رقم در خروجی باقی بماند.

• اعدادی که خروجی نهایی آن ها برابر با 1 باشد، اعداد خوشحال هستند.

پ.ن:. تنها ورودی مجاز برای این برنامه اعداد صحیح مثبت هستند.

پ.ن:. برای جلوگیری از به دام افتادن در حلقه بی نهایت ماکزیمم تکرار الگوریتم را برابر 200 قرار دهید. 

---

### 🔹 Question 2 – q2_happy_num_chart.vsdx _ عدد خوشحال )ادامه(
*Description:*  

برای الگوریتم سوال قبل فلوچارت آن را طراحی و بیان کنید که برای اجرای آن از چه نوع control flow استفاده نموده اید.

Control flow used: conditional loop (while), decision-making (if), and return statement. A set is used for cycle detection to avoid infinite loops.

---

### 🔹 Question 3 – q3_motarjem.py _ مترجم آنالین
*Description:*  

سر کار از اکبر خواستن یه مترجم آنالین براشون بنویسه. مترجم آنالینی که اکبر میخواد آماده کنه یک دیکشنری داره و در انتها این برنامه باید یک جمله رو ترجمه کنه.

در خط اول ورودی یک عدد n وجود دارد که نمایانگر تعداد کلمات دیکشنری است. هر یک از n خط بعدی شامل دو کلمه است که کلمه دوم معنی کلمه اول می باشد. خط بعدی شامل یک جمله می باشد که هر کلمه آن با یک فاصله جدا شده اند. به اکبر کمک کنید و مترجمی بنویسید که ورودی های مربوطه را خوانده و جمله را ترجمه کند. در طی ترجمه اگر کلمه ای در جمله وجود داشت که در دیکشنری معنی آن وجود نداشت، خود کلمه را در خروجی چاپ کنید. 

ورودی نمونه:

5

hello salam

goodbye khodafez

say goftan

we ma

you shoma

we say goodbye to you tonight

خروجی:

ma goftan khodafez to shoma tonight

---

### 🔹 Question 4 – q4_normal_sazi.py _ نرمال سازی
*Description:*  

توی درس یادگیری ماشین از اکبر خواستن که تابعی پیادهسازی کنه که وقتی مجموعه ای از اعداد رو بهش میدیم همه اون اعداد رو به بازه 0 تا 1 تغییر مقیاس بده (به طوری که همه اعداد تو بازه 0 تا 1 بشن). برای نرمال سازی از رابطه زیر پیروی کنید.

Z_i = X_i - X_min / X_max - X_min

---

### 🔹 Question 5 – q5_list_target.py _  جستجوی محل درج 
*Description:*  

فرض کنید یک لیست مرتب شده )از کوچک به بزرگ( و یک عدد صحیح target به شما داده شده اس ت. تابعی بنویسید که عدد داده شده را در لیست جستجو و ایندکس آن را برگرداند. در صورتی که عدد داده شده در لیست موجود نبود، ایندکس محلی که انتظار میرفت که در آن وجود داشته باشد را برگرداند .

ورودی نمونه:

List = [1, 3, 5, 6] target = 5

خروجی:

2

---

### 🔹 Question 6 – q6_kahesh_be_0.py _ کاهش به صفر
*Description:*  

فرض کنید یک عدد صحیح به شما داده شده است، برنامه ای بنویسید که گام های الزم برای کاهش آن به صفر را شمارش کند. در هر گام، اگر عدد فعلی زوج بود آن را ت قسیم بر 2 و اگر فرد بود 1 واحد از آن کم شود.

ورودی نمونه:

14

خروجی:

6

---

### 🔹 Question 7 – q7_cityA_cityB.py _ شهر مقصد
*Description:*  

لیستی با نام paths به شما داده شده است که هر عنصر این لیست به صورت [cityB ,cityA]=[i[path می باشد و به این معنا است که مسیری مستقیم از cityA به cityB موجود می باشد . از شما خواسته شده است که تابعی بنویسید که این مسیرهارا از ورودی دریافت و ش هر مقصد را برگرداند (شهری که از آن هیچ مسیر خروجی وجود نداشته باشد)

---

## 📝 Notes
If a word or concept is not covered in the dictionary or logic, it will default to the original word/value.  
These exercises were written as part of my learning path in Python 🚀
