import streamlit as st
st.title("Password generator")
st.write("This script lets you choose the number of each digit type in your password and generates a password with the desiresd specifications\n")


def main():
    import random as r
    import pyperclip

    numlen = int(st.select_slider(
        "How many numbers does your password include? ", [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    charlen = int(st.select_slider(
        "How many characters does your password include? ", [2, 3, 4, 5, 6, 7, 8, 9]))
    symlen = int(st.select_slider(
        "How many symbols does your password include? ", [1, 2, 3, 4, 5, 6, 7, 8, 9]))

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
    st.markdown("### Your **:blue[Password]** is: ")
    pyperclip.copy(pass_string)
    st.header(pass_string)


if __name__ == "__main__":
    main()
