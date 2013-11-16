#!/usr/bin/env python
# Copyright (c) 2012, BSD-3 clause, Sunlight Labs

from sunlight import capitolwords
from sunlight import congress

phrase = "obamacare"
# Today, we'll be printing out the Twitter IDs of all legislators that use
# this phrase most in the congressional record.

for cw_record in capitolwords.phrases_by_entity(
    "legislator",   # We're getting all legislators
    sort="count",   # sorted by how much they say
    phrase=phrase,  # this word
)[:6]:  # We'll just try the top 5 legislators

    legislator = congress.legislators(
        bioguide_id=cw_record['legislator'],
        #  Look up this biogude (unique ID) for every fed. legislator
        all_legislators="true"  # search retired legislators
    )
    if len(legislator) >= 1:  # If we were able to find the legislator
        legislator = legislator[0]  # (this is a search, so it's a list)
        if legislator['twitter_id'] is not None:  # and they have a Twitter ID
            print "%s. %s (@%s) said %s %s times" % (
                legislator['title'],
                legislator['last_name'],
                legislator['twitter_id'],
                phrase,
                int(cw_record['count'])
            )  # Print it to output :)
