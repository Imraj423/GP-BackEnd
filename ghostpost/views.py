from ghostpost.models import ghostPost
from rest_framework import viewsets
from ghostpost import models, serializers


class GhostPost_view(viewsets.ModelViewSet):

    queryset = models.ghostPost.objects.all()
    serializer_class = serializers.GhostPost_Serializer

### add endpoins for upvote and downvotes