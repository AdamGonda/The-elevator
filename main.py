import re

def main(floors):
    result = []
    for item in floors.split(','):
        matches = re.match(r'(-?\d+)-?(-?\d+)?', item.strip())
        n1 = matches.group(1)
        n2 = matches.group(2)
        result.extend(list(range(int(n1), int(n2 or n1) + 1)))
    return sorted(set(result))


if __name__=='__main__':
    floors = '-1, 2, -7--1'
    print(main(floors))
