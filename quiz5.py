def reverse_integer(num):
    sign = -1 if num < 0 else 1
    num = abs(num)
    reversed_num = int(str(num)[::-1])
    return sign * reversed_num

print(reverse_integer(500)) # returns 5
print(reverse_integer(-56)) # returns -65
print(reverse_integer(-90)) # returns -9
print(reverse_integer(91)) # returns 19