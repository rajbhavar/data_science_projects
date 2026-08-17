arr = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(arr)
total = (n + 1) * (n + 2) // 2

actual_sum = 0
for num in arr:
    actual_sum += num

missing = total - actual_sum

print(missing)