import re

def get_range(n1, n2):
    return list(range(min(int(n1), int(n2)), max(int(n1), int(n2)) + 1))

def calc_floors(item):
    if item.find('--') > 0:
        n1 = re.match(r'(\A-?\d*)', item).group() 
        rest = item[len(n1):]
        n2 = rest[1:]
        return get_range(n1, n2)
    
    else:
        n1 = re.match(r'(\A-?\d*)', item).group()
        rest = item[len(n1):]
        if len(rest) > 0:
            n2 = rest[1:]
            return get_range(n1, n2)

        return int(n1)

def main(floors):
    result = []
    for item in floors.split(','):
        r = calc_floors(item.strip())
        try:
            result.extend(r)
        except:
            result.append(r)

    return sorted(set(result))


if __name__=='__main__':
    floors = '-16, 1, 1-7, -4-6, -1--4, 4--7'
    print(main(floors))
