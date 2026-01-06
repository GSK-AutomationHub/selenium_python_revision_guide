
def get_fibonacci_series(till_no:int):
    a,b = 0,1
    if till_no <=0:
        print("please enter valid positive integer term")
    elif till_no ==1:
        print("fib series for given term is: ", a)
    else:
        print(f"Fibonacci sequence up to {till_no} terms:")
        print(a, end=' ')
        print(b, end=' ')
        count = 0
        while count < till_no:
            nth = a + b
            print(nth, end=' ')
            a=b
            b=nth
            count+=1

get_fibonacci_series(15)
