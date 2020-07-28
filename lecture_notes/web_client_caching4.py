# Build a "client" that will cache a URL

## First request: go out to the internet, get the web page
## Second request: return from cache

# How to implement using a hash table?
## What are our keys?   URL!
## What are our values?   web page data!

import urllib.request
import datetime

cache = {}
url = "https://www.google.com"

class CacheEntry:
    def __init__(self, data):
        self.data = data
        self.time_fetched = datetime.datetime.now().timestamp()


def fetch_web_page(url):
### given a url, check if it's in the cache
    stale_data = True
    if url in cache:
        time_now = datetime.datetime.now().timestamp()
        print("Getting from cache")
        cache_entry = cache[url]

        if time_now - cache_entry.time_fetched < 10:
            page = cache_entry.data
            stale_data = False

    elif stale_data:
        print("getting from the internetz")
### otherwise, send out a request to get the web page
        response = urllib.request.urlopen(url)
        data = response.read()
        response.close()

#### and put the result in our cache
        cache_entry = CacheEntry(data)
        cache[url] = cache_entry
        page = cache[url].data

    return page

page = fetch_web_page(url)
print(page)

also_page = fetch_web_page(url)

# One issue: memory usage, lots of URLs will fill memory up
## If the page isn't requested in awhile, delete
## LRU cache
## Use time to delete really old data

# What if the page changes?
## Store time, and if data is stale, re-fetch