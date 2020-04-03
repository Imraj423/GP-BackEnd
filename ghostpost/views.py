from ghostpost.models import ghostPost
from rest_framework import viewsets, permissions
from ghostpost import models, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.forms import model_to_dict



class GhostPost_view(viewsets.ModelViewSet):

    queryset = models.ghostPost.objects.all()
    serializer_class = serializers.GhostPost_Serializer
    permission_classes = [
        permissions.AllowAny
    ]

    @action(detail=True, methods=['GET'])
    def upvote(self, request, pk=None):
        upvote = ghostPost.objects.get(pk=pk)
        upvote.total_count += 1
        upvote.save()
        return Response({'status': 'Shine'})

    @action(detail=True, methods=['GET'])
    def downvote(self, request, pk=None):
        downvote = ghostPost.objects.get(pk=pk)
        downvote.total_count -= 1
        downvote.save()
        return Response({'status': 'Shade!'})

    @action(detail=True, methods=['delete'])
    def remove(self, request, pk=None):
        post_res = None
        try:
            post = ghostPost.objects.get(secret_id=pk)
            post_res = model_to_dict(post)['id']
            post.delete()
        except Exception as e:
            return Response({'error': f"{e}"})
        return Response({post_res})
