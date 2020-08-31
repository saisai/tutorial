
width = 5

for num in range(0, 100):
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

