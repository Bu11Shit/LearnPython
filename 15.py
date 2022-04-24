# 분자
numerator = 1
# 분모
denominator = 3

maxNum = 101
count = 0

n = 2
Sum_ = 0
for i in range(0, maxNum):
    if i % 2 == 0:
        count += 1

for i in range(denominator, maxNum + n, n):
    if i > numerator:
        Sum_ += float(numerator / i)
        numerator += 2

print(Sum_)

