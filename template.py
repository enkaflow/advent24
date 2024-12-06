import csv

def main():
    with open("in.txt", "r") as f:
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            print(row)
    

    print("---")



if __name__ == "__main__":
    main()
