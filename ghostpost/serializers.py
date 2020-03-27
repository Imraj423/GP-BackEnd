from ghostpost import models
from rest_framework import serializers


class GhostPost_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ghostPost
        fields = ['message', 'time', 'is_Boast', 'upvote', 'downvote']
