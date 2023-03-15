for _ in range(int(input())):
    res = 0
    n, c = list(map(int, input().split()))
    planets = list(map(int, input().split()))
    orbit_count = [0] * (max(planets) + 1)
    for pos in planets:
        orbit_count[pos] += 1
    for count in orbit_count:
        if count > c:
            res += c
        else:
            res += count
    print(res)
