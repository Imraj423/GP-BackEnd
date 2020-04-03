from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


class ghostPost(models.Model):
    message = models.CharField(max_length=280)
    time = models.DateTimeField(default=timezone.now)
    is_Boast = models.BooleanField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    total_count = models.IntegerField(default=0)
    secret_id = models.CharField(default=None, null=True, max_length=6)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        is_unique = False
        while not is_unique:
            secret_id = get_random_string(length=6)
            try:
                ghostPost.objects.get(secret_id=secret_id)
            except Exception:
                is_unique = True
        self.secret_id = secret_id
        return super(ghostPost, self).save(*args, **kwargs)
