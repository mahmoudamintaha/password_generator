
def strong_pass():
    import random as r

    while True:
        try:
            numlen = int(
                input("\n How many numbers does your password include? "))
            break
        except:
            print("\n Wrong input, you should type a whole number! ")
            continue

    while True:
        try:
            charlen = int(
                input("\n How many characters does your password include? "))
            break
        except:
            print("\n Wrong input, you should type a whole number! ")
            continue

    while True:
        try:
            symlen = int(
                input("\n How many symbols does your password include? "))
            break
        except:
            print("\n Wrong input, you should type a whole number! ")
            continue

    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "1", "2", "3",
            "4", "5", "6", "7", "8", "9", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    upper_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                     "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lower_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    symbols = ["#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "="]

    numf = r.sample(nums, numlen)
    ucharf = r.sample(upper_letters, charlen-1)
    lcharf = r.sample(lower_letters, 1)
    symf = r.sample(symbols, symlen)

    pass_list = numf + ucharf + lcharf + symf
    r.shuffle(pass_list)
    r.shuffle(pass_list)
    r.shuffle(pass_list)
    r.shuffle(pass_list)

    pass_string = ''.join(str(e) for e in pass_list)
    print("\n Your Password is: {}  ".format(pass_string))

    answer = input("\n Would you like some other password? ")
    if answer == "yes":
        strong_pass()
    else:
        print("\n program ended ")


if __name__ == "__main__":
    strong_pass()
