from django.test import TestCase

# Create your tests here.

from trackQueue.databaseIO import IO

io = IO()
testInput = {
   'comment':'',
   'rating':'0',
   'albumArtRef':[
     {
       'url': 'http://lh6.ggpht.com/...'
     }
   ],
   'artistId':[
     'Aod62yyj3u3xsjtooghh2glwsdi'
   ],
   'composer':'',
   'year':2011,
   'creationTimestamp':'1330879409467830',
   'id':'5924d75a-931c-30ed-8790-f7fce8943c85',
   'album':'Heritage ',
   'totalDiscCount':0,
   'title':'Haxprocess',
   'recentTimestamp':'1372040508935000',
   'albumArtist':'',
   'trackNumber':6,
   'discNumber':0,
   'deleted':False,
   'storeId':'Txsffypukmmeg3iwl3w5a5s3vzy',
   'nid':'Txsffypukmmeg3iwl3w5a5s3vzy',
   'totalTrackCount':10,
   'estimatedSize':'17229205',
   'albumId':'Bdkf6ywxmrhflvtasnayxlkgpcm',
   'beatsPerMinute':0,
   'genre':'Progressive Metal',
   'playCount':7,
   'artistArtRef':[
     {
       'url': 'http://lh3.ggpht.com/...'
     }
   ],
   'kind':'sj#track',
   'artist':'Opeth',
   'lastModifiedTimestamp':'1330881158830924',
   'clientId':'+eGFGTbiyMktbPuvB5MfsA',
   'durationMillis':'418000'
 }
print("your previous track entries were:")
print(io.getTrackEntries())

print("\n inserting new track into database \n")

io.insertTrackData(1, testInput)

print("your current track entries are:")
print(io.getTrackEntries())

trackDetailsDict = io.getTrackDetails()
print(trackDetailsDict)

# print("\n returning track details about track: 5924d75a-931c-30ed-8790-f7fce8943c85 \n")
# trackDetailsDict = io.getTrackDetails("5924d75a-931c-30ed-8790-f7fce8943c85")
# print(trackDetailsDict)
#
# print("\n returning track id from track: Haxprocess \n")
# print(io.getTrackId("Haxprocess"))
#
# print("\n deleting track from database - track id: 5924d75a-931c-30ed-8790-f7fce8943c85 \n")
#
# io.deleteTrack("5924d75a-931c-30ed-8790-f7fce8943c85")
#
# print("your current track entries are:")
# print(io.getTrackEntries())