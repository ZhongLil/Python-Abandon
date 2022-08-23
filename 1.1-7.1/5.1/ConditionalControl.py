nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in nums:
    if num % 2 == 0:
        print(num)
print("\n")
for num in nums:
    if num % 2 != 0:
        print(num)
    elif num % 3 ==0:
        print(num)
    else:
        print("null")
print("\n")
for num in nums:
    if num % 2 != 0 and num % 3 == 0:
        print(num)
print("\n")
strings = {"a", "b", "c", "d"}
if "a" in strings:
    print("true")
