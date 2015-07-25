'''
Created on 25 Jul 2015

@author: akrv
'''
import mechanize
import downl0ad3r

def run():
    brow = mechanize.Browser()
    brow.set_handle_robots(False)   # no robots
    brow.set_handle_refresh(False)  # can sometimes hang without this
    brow.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    baseUrl = "http://www.einthusan.com/movies/index.php?lang=tamil&organize=Year&filtered=2015&org_type=Year"
    domain = "http://www.einthusan.com/movies/index.php"
    response = brow.open(baseUrl)
    paginationRange =[]
    for i in range(1,159):
        paginationRange.append(str(i))

    for link in brow.links():
        if link.text in paginationRange:
            br = mechanize.Browser()
            br.set_handle_robots(False)   # no robots
            br.set_handle_refresh(False)  # can sometimes hang without this
            br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
            response = br.open(domain+link.url)
            downl0ad3r.get4mPage(br)
        if link.text == str(158):
            print "here"
            break
