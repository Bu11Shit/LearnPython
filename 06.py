import math

# radian = 3.14 * degree / 180.0

print("degree\tsin\t\tcos")
print("=" * 40)

for degree in range(0, 91, 10):
    # print(math.sin(math.pi/2))
    sin = math.sin(math.pi * degree / 180)
    cos = math.cos(math.pi * degree / 180)
    print(f"{degree:2d}\t\t{sin:.3f}\t{cos:.3f}")



