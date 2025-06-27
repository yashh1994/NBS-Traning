from collections import defaultdict

def find_ramanujan_numbers(limit):
    cube_sums = defaultdict(list)
    max_val = int(limit ** (1/3)) + 1
    ctn = 0
    for a in range(1, max_val):
        for b in range(a, max_val-a+1):
            ctn += 1
            sum_cubes = a**3 + b**3
            if sum_cubes >= limit:
                break
            cube_sums[sum_cubes].append((a, b))

    ramanujan_numbers = []
    for val, pairs in cube_sums.items():
        if len(pairs) > 1:
            ramanujan_numbers.append((val, pairs))

    return sorted(ramanujan_numbers), ctn

nm = 10**6
ramanujan, ctn = find_ramanujan_numbers(nm)
print(f"For {nm} got Count {ctn}")
