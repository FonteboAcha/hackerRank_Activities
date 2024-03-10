if __name__ == '__main__':
    s = input()
    vals = {
        'alnum_count': 0,
        'alph_count': 0,
        'dig_count': 0,
        'low_count': 0,
        'up_count': 0,
    }
    for char in s:
        for n in range(5):
            if char.isalnum():
                vals['alnum_count'] += 1
            elif char.isalpha():
                vals['alph_count'] += 1
            elif char.isdigit():
                vals['dig_count'] += 1
            elif char.islower():
                vals['low_count'] += 1
            elif char.isupper():
                vals['up_count'] += 1

    for n in vals.values():
        if n:
            print(n)
            print("True")
        else:
            print(n)
            print("False")


