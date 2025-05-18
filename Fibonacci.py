def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci_recursive(n - 1)
        series.append(series[-1] + series[-2])
        return series


terms = int(input("Enter the number of terms in Fibonacci series: "))


print("Fibonacci series:")
print(fibonacci_recursive(terms))
