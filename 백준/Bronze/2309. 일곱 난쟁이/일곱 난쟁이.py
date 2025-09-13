dwarfs = [int(input()) for _ in range(9)]
total = sum(dwarfs)

found = False
for i in range(8):
    for j in range(i + 1, 9):
        if total - dwarfs[i] - dwarfs[j] == 100:
            fake1, fake2 = dwarfs[i], dwarfs[j]
            dwarfs.remove(fake1)
            dwarfs.remove(fake2)
            found = True
            break
    if found:
        break

dwarfs.sort()
for dwarf in dwarfs:
    print(dwarf)
