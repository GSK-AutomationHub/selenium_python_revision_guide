
def generate_fibonacci_series(term:int):
    a,b = 0,1
    if type(term) is not int:
        print("please enter integer value")
    elif term <= 0:
        print("please enter non zero value")
    elif term == 1:
        print(f"the fib series till count {term} is", a)
    else:
        count = 1
        print(a,b, end=' ')
        while count < term:
            n = a + b
            print(n, end=' ')
            a = b
            b = n
            count +=1

generate_fibonacci_series(12)