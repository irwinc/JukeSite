import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "login.settings")
django.setup()
from trackQueue.models import Track

class IO():
    """
    Class that contains methods to perform database interactions
    """
    def getTrackEntries(self):
        """
         returns list of track objects
        """
        return Track.objects.all()

    def insertTrackData(self, queuePosition, trackData):
        """
        passed a dictionary from gmusic api to insert track data
        """
        t = Track(queuePosition=queuePosition,
                  id=trackData.get('id'),
                  storeId=trackData.get('storeId'),
                  title=trackData.get('title'),
                  comment=trackData.get('comment'),
                  rating=trackData.get('rating'),
                  albumArtRef=trackData.get('albumArtRef'),
                  artistId=trackData.get('artistId'),
                  composer=trackData.get('composer'),
                  year=trackData.get('year'),
                  creationTimestamp=trackData.get('creationTimestamp'),
                  album=trackData.get('album'),
                  totalDiscCount=trackData.get('totalDiscCount'),
                  recentTimestamp=trackData.get('recentTimestamp'),
                  albumArtist=trackData.get('albumArtist'),
                  trackNumber=trackData.get('trackNumber'),
                  discNumber=trackData.get('discNumber'),
                  deleted=trackData.get('deleted'),
                  nid=trackData.get('nid'),
                  totalTrackCount=trackData.get('totalTrackCount'),
                  estimatedSize=trackData.get('estimatedSize'),
                  albumId=trackData.get('albumId'),
                  beatsPerMinute=trackData.get('beatsPerMinute'),
                  genre=trackData.get('genre'),
                  playCount=trackData.get('playCount'),
                  artistArtRef=trackData.get('artistArtRef'),
                  kind=trackData.get('kind'),
                  artist=trackData.get('artist'),
                  lastModifiedTimestamp=trackData.get('lastModifiedTimestamp'),
                  clientId=trackData.get('clientId'),
                  durationMillis=trackData.get('durationMillis'))
        t.save()

    def deleteTrack(self, id):
        """
        deletes track matching the passed id 
        """
        Track.objects.filter(id=id).delete()

    def getTrackDetails(self, id):
        """
        returns track details from track matching the passed id
        :param id: 
        :return: 
        """
        return Track.objects.filter(id=id).values()[0]

    def getTrackDetails(selfs):
        """
        returns track details from every track in the database
        :return: 
        """
        return Track.objects.all().values()[0]

    def getTrackId(self, title):
        """
        returns track id from track with the matching passed title
        :param title: 
        :return: 
        """
        return Track.objects.filter(title=title).values()[0].get('id')