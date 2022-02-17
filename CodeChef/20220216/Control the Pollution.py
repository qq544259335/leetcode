for _ in range(int(input())):
    n, bus, car = list(map(int, input().split()))
    if bus / 100 >= car / 4:
        time = n // 4 if n % 4 == 0 else n // 4 + 1
        print(car * time)
        continue
    time = 0
    price = 0
    if n >= 100:
        time += n // 100
        n -= time * 100
        price += time * bus
    car_time = n // 4 if n % 4 == 0 else n // 4 + 1
    car_price = car * car_time
    price = price + car_price if car_price < bus else price + bus
    print(price)
