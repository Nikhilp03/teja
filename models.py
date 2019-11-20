from django.db import models
import datetime
class notes_note(models.Model):
    title = models.CharField(max_length= 150)
    descrpition = models.CharField(max_length= 150)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
