def fibo(n):
    series = [0, 1]
    while len(series) < n:
        next_term = series[-1] + series[-2] 
        series.append(next_term)
    return series
num_terms=int(input("Enter the number of series to show "))
fibo_series = fibo(num_terms)
print("Fibonacci series of", num_terms,"is")
for term in fibo_series:
    print(term, end=" ")

