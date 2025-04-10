def find_destination_city(paths):
    # استخراج شهرهایی که به عنوان مبدا هستند (cityA)
    cities_with_outgoing_paths = {path[0] for path in paths}
    
    # استخراج شهرهایی که به عنوان مقصد هستند (cityB)
    cities_with_incoming_paths = {path[1] for path in paths}
    
    # پیدا کردن شهری که در cities_with_incoming_paths هست ولی در cities_with_outgoing_paths نیست
    destination_city = cities_with_incoming_paths - cities_with_outgoing_paths
    
    return destination_city.pop() if destination_city else None

# ورودی نمونه اول:
# paths = [['Tehran', 'Saveh'], ['Saveh', 'Isfahan'], ['Isfahan', 'Shiraz']]
# print(find_destination_city(paths))  # خروجی: 'Shiraz'

# ورودی نمونه دوم:
# paths = [['B', 'D'], ['A', 'C'], ['C', 'B']]
# print(find_destination_city(paths))  # خروجی: 'D'

# دریافت ورودی از کاربر
paths = []
while True:
    path_input = input("Enter a path as 'cityA cityB' or type 'done' to finish: ")
    if path_input.lower() == 'done':
        break
    else:
        # تجزیه ورودی به دو بخش cityA و cityB
        cityA, cityB = path_input.split()
        paths.append([cityA, cityB])

# فراخوانی تابع برای پیدا کردن شهر مقصد
destination_city = find_destination_city(paths)

# چاپ نتیجه
if destination_city:
    print(f"The destination city is: {destination_city}")
else:
    print("No destination city found.")