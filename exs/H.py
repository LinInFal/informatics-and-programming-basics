def is_right_triange(x1, y1, x2, y2, x3, y3):
    AB2 = (x2-x1) ** 2 + (y2-y1) ** 2
    AC2 = (x3-x1) ** 2 + (y3-y1) ** 2
    BC2 = (x3-x2) ** 2 + (y3-y2) ** 2
    return (AB2 + AC2 == BC2) or (AB2 + BC2 == AC2) or (AC2 + BC2 == AB2)

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if is_right_triange(x1, y1, x2, y2, x3, y3):
    print("YES")
else:
    print("NO")