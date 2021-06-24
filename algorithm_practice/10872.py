def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# n이 1보다 작거나 같으면 1을 return
# 그 외에 경우 n * factorial(n - 1)

t = int(input())
print(factorial(t))
