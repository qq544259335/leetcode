a, b, c, d = list(map(int, input().split()))
y = c / b
if y.is_integer():
    y = int(y)
else:
    y = int(y) + 1


def get_x():
    return (d + y * b) / a


decimal_set = set()
while not get_x().is_integer():
    y += 1
    _, dec = divmod(get_x(), 1)
    if dec in decimal_set:
        print("No solution.")
        exit()
    decimal_set.add(dec)
x = int(get_x())
boat = " boat" if y == 1 else " boats"
truck = " truck " if x == 1 else " trucks "
print("We need " + str(x) + truck + "and " + str(y) + boat + ".")
