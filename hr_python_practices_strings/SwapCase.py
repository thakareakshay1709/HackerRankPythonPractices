def swap_case(s):
    s2 = ""
    for i in s:
        if i.islower():
            i = i.capitalize()
            s2 = s2 + i
        elif i.isupper():
            i = i.lower()
            s2 = s2 + i
        else:
            s2 = s2 + i
    return s2


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
