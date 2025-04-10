def search_insert_position(my_list, target):
    left, right = 0, len(my_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if my_list[mid] == target:
            return mid
        elif my_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left  # This is the index where target should be inserted

# گرفتن ورودی‌ها از کاربر
my_list = list(map(int, input("Enter your numbers (space-separated): ").split()))
target = int(input("Enter your target number: "))

# پیدا کردن ایندکس با استفاده از جستجوی باینری
index = search_insert_position(my_list, target)
print("The index is:", index)