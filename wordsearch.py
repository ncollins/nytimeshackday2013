# Modified from example:
# http://sunlightfoundation.com/blog/2012/02/13/introducing-python-sunlight/
# Copyright (c) 2012, BSD-3 clause, Sunlight Labs

from sunlight import capitolwords
from sunlight import congress
import sunlight

from login import keys

sunlight.config.API_KEY = keys['sunlight']

phrase = 'the'  # input_phrase
start_date = '2011-10-05'  # input_date - 183
end_date = '2013-11-16'  # input_date + 183
legislator_id = 'K000352'  # input_bioguide_id

# return the count of how many times a certain legislator used
# this phrase in the congressional record during a period of time.


def count_phrase_for_legislator(phrase, legislator_id, start_date, end_date):

    for cw_record in capitolwords.phrases_by_entity(
        "legislator",   # We're getting all legislators
        # bioguide=legislator_id,
        phrase=phrase,  # this word
        start_date=start_date,
        end_date=end_date,
        sort="count",   # sorted by how much they say
    )[:]:

        legislator = congress.legislators(
            bioguide_id=cw_record['legislator'],
            #  Look up this biogude (unique ID) for every fed. legislator
            all_legislators="true"  # search retired legislators
        )

        if len(legislator) >= 1:  # If we were able to find the legislator
            legislator = legislator[0]  # (this is a search, so it's a list)
            if cw_record['legislator'] == legislator_id:
                # print("%s. %s said %s %s times" % (
                #     legislator['title'],
                #     legislator['last_name'],
                #     phrase,
                #     int(cw_record['count']))
                #     )
                return (legislator['title'] + ' ' +legislator['last_name'], int(cw_record['count']))
        return (legislator['title'] + ' ' +legislator['last_name'], int(cw_record['count']))
    return ('', 0)

print(count_phrase_for_legislator(phrase, legislator_id, start_date, end_date))
