# Modified from example:
# http://sunlightfoundation.com/blog/2012/02/13/introducing-python-sunlight/
# Copyright (c) 2012, BSD-3 clause, Sunlight Labs

from sunlight import capitolwords
from sunlight import congress

phrase = 'health'  # input_phrase
date_start = '2013-10-05'  # input_date - 183
date_end = '2013-10-05'  # input_date + 183
bioguide_id = 'K000352'
# Today, we'll be printing out the names of all legislators that use
# this phrase most in the congressional record during a period of time.


def count_phrase_for_legislator(phrase, bioguide_id, date_start, date_end):

    for cw_record in capitolwords.phrases_by_entity(
        "legislator",   # We're getting all legislators
        sort="count",   # sorted by how much they say
        phrase=phrase,  # this word
        legislator=bioguide_id
    )[:6]:

        legislator = congress.legislators(
            bioguide_id=cw_record['legislator'],
            #  Look up this biogude (unique ID) for every fed. legislator
            all_legislators="true"  # search retired legislators
        )

        if len(legislator) >= 1:  # If we were able to find the legislator
            legislator = legislator[0]  # (this is a search, so it's a list)

            print("%s. %s said %s %s times" % (
                legislator['title'],
                legislator['last_name'],
                phrase,
                int(cw_record['count']))
            )  # Print it to output :)

count_phrase_for_legislator(phrase, bioguide_id, date_start, date_end)
