sunlight-foundation
===================

Goal; Compute the complexity of each bill in congress. As a first crack, measure the number of references to laws. Usually, such references are particularly obscure.
There is  not an easily-recognizable grammar to recognize legal citations inline, but a few common words will suffice for startsers;
"United States Code", "Federal Register", U.S.C., "Public Law", "Private Law"



nytimeshackday2013
==================

NYT Developers Hack Day 2013-11-16

To use this you need a `login.py` file that looks like this:

```
keys = {
    'nyt_article_search': '***',
    'nyt_campaign_finance': '***',
    'nyt_congress': '***',
    'sunlight': '***',
}
```

You can get a key from [developer.nytimes.com/register](developer.nytimes.com/register)
and [http://sunlightfoundation.com/api/](http://sunlightfoundation.com/api/).
