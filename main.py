
import csv

CSV_FILE = 'bills.csv'

def main():
    with open(CSV_FILE) as data_file:
        reader = csv.reader(data_file)
        for row in reader:
            print(row)

if __name__ == '__main__':
    main()
