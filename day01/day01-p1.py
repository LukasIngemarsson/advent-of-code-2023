line = input()
sum = 0
while line:
    for c in line: # find first digit
        if c.isdigit():
            first = int(c)
            break
    for c in line[::-1]: # find last digit (search in reverse)
        if c.isdigit():
            last = int(c)
            break
    sum += 10 * first + last
    line = input()
print(sum)