from urllib.request import urlopen
from xml.etree.ElementTree import parse

# download rss feed and parse it
u = urlopen('http://planetpython.org/rss20.xml')
doc = parse(u)  # top level rss element

# extract and ouput tags of interest
# look for all item elements under a channel elemment
for item in doc.iterfind('channel/item'):
    # findnext relative to the found item elements
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()

