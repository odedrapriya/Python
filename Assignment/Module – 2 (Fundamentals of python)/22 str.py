def string_both_ends(str):
 if len(str) < 2:
    return ' '

    return str[0:2] + str[-2:]

print(string_both_ends('harsh'))
print(string_both_ends('ha'))
print(string_both_ends('h'))