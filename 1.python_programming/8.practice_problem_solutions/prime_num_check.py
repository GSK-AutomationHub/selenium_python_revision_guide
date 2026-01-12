# prime number : number that get divided by itself and 1 only

def check_prime_number(num:int):
    if type(num) != int or num < 2:
        print("Please provide an integer number greater than 1")
    elif num > 2:
        for i in range(2, num):
            if num % i == 0:
                print(f"You submitted number {num} & it's not a prime number")
                break
        else:
            print(f"You submitted number {num} & it's a prime number")


check_prime_number(11)