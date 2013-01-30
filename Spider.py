#-------------------------------------------------------------------------------
# Name:        Model_Spider
# Purpose:
#
# Author:      shuson
#
# Created:     30/01/2013
# Copyright:   (c) shuson 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# get html source code
import urllib2
def get_page(url):
    source = urllib2.urlopen(url)
    return source.read()

# get next pattern of link
def get_next_target(page):
    start_link=page.find('<a href=')
    if start_link==-1:
        return None,0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote+1:end_quote]
    return url,end_quote
# get all links in this page
def get_all_link(page):
    while True:
        url,end_pos = get_next_target(page)
        if url:
            print url
            page = page[end_pos:]
        else:
            break
#outer port method
def print_link(url):
    get_all_link(get_page(url))
