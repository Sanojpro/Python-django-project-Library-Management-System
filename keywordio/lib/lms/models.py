#Project Library Management System
#---SANOJ KUMAR PRADHAN---#


from django.db import models

#created Book model to create table in the database having the columns(BID,NAME,AUTHOR,PUBLISHER)
class Book(models.Model):
    BID=models.AutoField(primary_key=True,editable=False)
    NAME=models.CharField(max_length=100)
    AUTHOR=models.CharField(max_length=70)
    PUBLISHER=models.CharField(max_length=70)