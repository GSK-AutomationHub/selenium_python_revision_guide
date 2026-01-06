
def detect_even_odd(input):
    if type(input) != int:
        print("please provide integer number")
    elif input % 2 ==0:
        print(f"You submitted number {input} & it's an even number")
    else:
        print(f"You submitted number {input} & it's an odd number")



detect_even_odd(24)