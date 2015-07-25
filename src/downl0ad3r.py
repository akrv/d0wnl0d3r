'''
Created on Jul 24, 2015

@author: akrv
'''

import requests
from urlparse import urlparse
import urllib,os
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('southpaw.in', 27017)
db = client.d0wnl0ad3r
collection = db.movie_collection

getFile = "http://hostmasterzone.com/beta/getDownloadLink.php?q="
baseURL = "http://www.einthusan.com"

def dataInDB(document):
    collection.insert_one(document)

def checkMovie(document):
    result = collection.find_one({'movieName':document['movieName']})
    if result == None:
        return True
    else:
        return False

def downloadMovie(movieFileURL, movieName):
    directory = movieName
    if not os.path.exists(directory):
        os.makedirs(directory)
    urllib.urlretrieve(movieFileURL, movieName+"/"+movieName+".mp4")

def get4mPage(br):
    for link in br.links():
        document = {}
        if link.url[0:9]=="../movies":
            movieURL = baseURL+link.url[1:len(link.url)]
            o = urlparse(movieURL).query.split("=")
            if len(o) == 4:
                movieName =      o[1].split("&")[0].replace("+"," ")
                movieLanguage =  o[2].split("&")[0]
                movieID =        o[3]
                requestURL = getFile+urllib.quote(movieURL,safe='')
                movieFileURL = requests.get(requestURL).content
                document = {
                            'movieName'         :   movieName,
                            'movieLanguage'     :   movieLanguage,
                            'movieID'           :   int(movieID),
                            'requestURL'        :   requestURL,
                            'downloadURL'       :   movieFileURL,
                            'downloadType'      :   'd0wnl0ad3r'
                            }
                print document
                if checkMovie(document) == True:
                    print "checked"
                    downloadMovie(movieFileURL, movieName)
                    dataInDB(document)
