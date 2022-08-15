from rest_framework import serializers
from places.models import Place
from comments.models import Comment


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Place
        fields ='__all__'

class PlaceListCommentSerializer(serializers.ModelSerializer):

    comment = serializers.SerializerMethodField()

    class Meta:

        model = Place
        fields =(
            'id',
            'name',
            'comment',
        )