from django.db import models
from django.utils import timezone
from vote.models import VoteModel


class ghostPost(VoteModel, models.Model):
    message = models.CharField(max_length=280)
    time = models.DateTimeField(default=timezone.now)
    is_Boast = models.BooleanField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    total_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.message
