from django.db import models

class Track(models.Model):
    """
    database table containing track information
    """
    queuePosition = models.IntegerField(default=-1)
    id = models.CharField(max_length=256, primary_key=True, default=-1)
    storeId = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    comment = models.CharField(max_length=256)
    rating = models.CharField(max_length=256)
    albumArtRef = models.CharField(max_length=1024)
    artistId = models.CharField(max_length=256)
    composer = models.CharField(max_length=256)
    year = models.IntegerField(default=0)
    creationTimestamp = models.CharField(max_length=256)
    album = models.CharField(max_length=256)
    totalDiscCount = models.IntegerField(default=0)
    recentTimestamp = models.CharField(max_length=256)
    albumArtist = models.CharField(max_length=256)
    trackNumber = models.IntegerField(default=0)
    discNumber = models.IntegerField(default=0)
    deleted = models.BooleanField(default=0)
    nid = models.CharField(max_length=256)
    totalTrackCount = models.IntegerField(default=0)
    estimatedSize = models.CharField(max_length=256)
    albumId = models.CharField(max_length=256)
    beatsPerMinute = models.IntegerField(default=0)
    genre = models.CharField(max_length=256)
    playCount = models.IntegerField(default=0)
    artistArtRef = models.CharField(max_length=1024)
    kind = models.CharField(max_length=256)
    artist = models.CharField(max_length=256)
    lastModifiedTimestamp = models.CharField(max_length=256)
    clientId = models.CharField(max_length=256)
    durationMillis = models.CharField(max_length=256)

    def __str__(self):
        return self.title

