ip = "192.168.1.300"


def is_valid(string):
    number = string.split('.')
    counter = 0

    for num in number:
        if num.isdigit():
            if num[0] != '0' or (len(num) == 1 and num == '0'):
                if 0 <= int(num) <= 255:
                    counter += 1
    return counter == 4

print(is_valid(ip))