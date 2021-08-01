generated_strings = []


def generate_binary_strings(bits, current_str=""):
    if bits < 1:
        generated_strings.append(current_str)
    else:
        generate_binary_strings(bits - 1, current_str + "0")
        generate_binary_strings(bits - 1, current_str + "1")


def generate_strings(bits, chars=None, current_str=""):
    if chars is None:
        chars = []
    if bits < 1:
        generated_strings.append(current_str)
    else:
        for char in chars:
            generate_strings(bits - 1, chars, current_str + char)


if __name__ == '__main__':
    symbols = ['a', 'b', 'c']
    generate_strings(1, symbols)
    print(generated_strings)
    generated_strings = []
    generate_strings(2, symbols)
    print(generated_strings)
    generated_strings = []
    generate_strings(3, symbols)
    print(generated_strings)
