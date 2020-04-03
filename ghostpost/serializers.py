from ghostpost import models
from rest_framework import serializers


class GhostPost_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.ghostPost
        fields = ['id','message', 'time', 'is_Boast', 'upvote', 'downvote', 'total_count']
