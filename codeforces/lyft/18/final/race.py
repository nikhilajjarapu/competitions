n = int(input())
x, y = list(map(int, input().split()))
d0 = max(x - 1, y - 1)
d1 = max(n - x, n - y)
print('White' if d0 <= d1 else 'Black')