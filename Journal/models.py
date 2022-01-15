from django.db import models

# Create your models here.

class Articles(models.Model):
    text = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    genre_id = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey('Authors', models.DO_NOTHING, blank=True, null=True)
    release = models.ForeignKey('Releases', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'articles'


class Authors(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'


class Genres(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    genre_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'



class Releases(models.Model):
    quantity = models.IntegerField(blank=True, null=True)
    actual = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'releases'

