
def check_if_palindrome(input_string):
    reversed_string = "".join(reversed(input_string))
    if input_string == reversed_string:
        print(f"{input_string} is palindrome")
    else:
        print(f"{input_string} is not palindrome")
    rev_str = ''
    result = [char + rev_str for char in input_string]
    print("".join(result))


check_if_palindrome("madam")