'''
Created on Jul 24, 2015

@author: akrv
'''
import mechanize
import requests
from urlparse import urlparse
import urllib

br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
baseUrl ="http://einthusan.com"
response = br.open(baseUrl)
getFile = "http://hostmasterzone.com/beta/getDownloadLink.php?q="
#Iterate the links
for link in br.links():
    #print link.text, link.url
    if link.url[0:8]=="./movies":
        movieURL = baseUrl+link.url[1:len(link.url)]
        o = urlparse(movieURL).query.split("=")
        if len(o) == 4:
            movieName =      o[1].split("&")[0].replace("+"," ")
            movieLanguage =  o[2].split("&")[0]
            movieID =        o[3]
            requestURL = getFile+urllib.quote(movieURL,safe='')
            movieFileUrl = requests.get(requestURL).content
            print movieName, movieFileUrl
            urllib.urlretrieve(movieFileUrl, movieName+".mp4")


            
#             http://hostmasterzone.com/beta/getDownloadLink.php?q=http://einthusan.com/movies/watch.php?tamilmoviesonline=Kakka+Muttai&lang=tamil&id=2659
#             http://hostmasterzone.com/beta/getDownloadLink.php?q=http://einthusan.com/movies/watch.php?tamilmoviesonline=Kakka+Muttai&lang=tamil&id=2659
#             http://hostmasterzone.com/beta/getDownloadLink.php?q=http%3A//einthusan.com/movies/watch.php%3Ftamilmoviesonline%3DKakka+Muttai%26lang%3Dtamil%26id%3D2659
