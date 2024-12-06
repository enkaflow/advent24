import csv
import math
from copy import copy

def main():
    reports = []
    with open("in.txt", "r") as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            reports.append(list(map(int, row)))
    
    count = 0
    for r in reports:
        if safe(r):
            count += 1
        else:
            for i in range(len(r)):
                c = copy(r)
                c.pop(i)
                if safe(c):
                    count += 1
                    break

    print(count)

def safe(report):
    is_incr = True
    is_decr = True
    satisfies_cond = True

    prev = report[0]
    for level in report[1:]:
        if level < prev:
            is_incr = False

        if level > prev:
            is_decr = False

        diff = abs(prev - level)
        if diff < 1 or diff > 3:
            return False

        prev = level

    if is_incr or is_decr:
        return True
        

if __name__ == "__main__":
    main()
