# every second number is multiplied with 2 and rest with 1
def multipliers(account_number):
    # print("multipliers work") # debug
    sum_digits = []

    # multipliers
    for idx, digit in enumerate(account_number):
        # 1x
        if idx % 2 == 0:
            times_one = sum_digits.append(int(digit) * 1)
        # 2x
        else:
            times_two = int(digit) * 2
            newnewnewnew = str(times_two)
            # if double digit (e.g. 18, then separate each digit and add together, like 1+8)
            if len(str(times_two)) >= 2:
                first_digit, second_digit = newnewnewnew[0], newnewnewnew[1]
                result = int(first_digit) + int(second_digit)
                sum_digits.append(result)
            # if single digit, then just do 2x
            else:
                sum_digits.append(times_two)
    return sum_digits

# check digit using the following equation: 
# (10 - (x % 10)) % 10 
# to get the digit
def check_digit(sum_digits):
    results_sum = sum(sum_digits)
    check_digit = (10-(results_sum % 10)) % 10
    return check_digit

# full account number
def full_number(account_number, next_check_digit):
    account_number = [i for i in account_number]
    add_last_digit = account_number.append(next_check_digit)
    # print(account_number, "account_number") # debugging
    complete_account_number = "".join([str(i) for i in account_number])
    return complete_account_number

# driver
def main():
    # change this as input, later
    account_number = "7992739871" # for testing purpose
    print("Initial account number given:", account_number)
    sum_digits = multipliers(account_number)

    # check digit
    next_check_digit = check_digit(sum_digits)
    print("Check digit is:", next_check_digit)

    # result
    print("Complete account number is:", full_number(account_number, next_check_digit))

if __name__ == "__main__":
    main()