file = open("input.txt", "r")
new_seq, ans = [], 0
for line in file:
    seq = [int(c) for c in line.split()]
    for i in range(1, len(seq)):
        new_seq.append(seq[i]-seq[i-1])
    # extrapolate new value, add to ans