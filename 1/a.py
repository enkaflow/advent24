import csv

def main():
    left = []
    right = []
    with open("in.txt", "r") as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            left.append(int(row[0]))
            right.append(int(row[-1]))
    

    left, right = sorted(left), sorted(right)
    sum = 0
#    for l, r in zip(left, right):
#print(f"comparing: {l}, {r}") 
#        sum += abs(l - r)

    for l in left:
        sum += l * right.count(l)

    print("---")
    print(sum)



if __name__ == "__main__":
    main()
