
import csv

from bill_search import count_matches, words

CSV_FILE = 'bills.csv'

def main():
    with open(CSV_FILE) as data_file:
        reader = csv.reader(data_file, quotechar='|') 
        for (congress, chamber, number, introduced_on, sponsor, title, file_path) in reader:
            with open(file_path) as f:
                print('{0}\nother documents: {1}'.format(title, count_matches(words, f.read())))


if __name__ == '__main__':
    main()
