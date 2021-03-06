
# Remove duplicate entries from a sequence while keeping order

def dedupe(items, key=None):
    seen = set()
    for item in items:
        #print(key(item))
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
    #print(seen)
if __name__ == '__main__':
    a = [
        {'x': 2, 'y': 3},
        {'x': 1, 'y': 4},
        {'x': 2, 'y': 3},
        {'x': 2, 'y': 3},
        {'x': 10, 'y': 15}
        ]
    print(a)
    print(list(dedupe(a, key=lambda a: (a['x'], a['y']))))
    print('\n\n')
    for k in dedupe(a, key=lambda a: (a['x'], a['y'])):
        print(k)
        print(k['x'], k['y'])

