def fib():
    fn1 = 0 # Current two consecutive fibonacci numbers
    fn2 = 1
    while True:
        current = fn1
        fn1, fn2 = fn2, fn1 + fn2
        yield current # yield a Fibonacci number

def main():
    iterator = fib()
    # Display all Fibonacci numbers <= 10000
    for i in iterator:
        if i <= 10000:
             print(i, end = ' ')
        else: break

main()