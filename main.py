
import csv
import datetime

from bill_search import count_matches, words, title_phrases
from wordsearch import count_phrase_for_legislator 

CSV_FILE = 'bills.csv'
TODAY = datetime.date.today().isoformat()

def main():
    with open(CSV_FILE) as data_file:
        i = 0
        reader = csv.reader(data_file, quotechar='|') 
        for (congress, chamber, number, introduced_on, sponsor, title, file_path) in reader:
            check_date = datetime.datetime.strptime(introduced_on, '%Y-%m-%d') - datetime.timedelta(90)
            if i > 200:
                break
            with open(file_path) as f:
                phrases = list(title_phrases(title)) + ['obamacare', 'clinton', 'war', 'jobs', 'budget', 'weapon', 'syria', 'military']
                print(file_path)
                print('{0}: {1}'.format(number, title))
                print('{0}: {1} other docs'.format(number, count_matches(words, f.read())))
                #print('{0}: sponsored by {1}'.format(number, sponsor))
                for p in phrases:
                        n, c = count_phrase_for_legislator(p, sponsor, check_date, TODAY)
                        if n not in ['Rep Gohmert', 'Sen Cruz', 'Sen Sessions', 'Rep Bachmann',
                                     'Rep King']:
                            print('{0}: {1} mentioned {2} {3} times'.format(number, n, p, str(c)))
                print('\n')
            i += 1


if __name__ == '__main__':
    main()
