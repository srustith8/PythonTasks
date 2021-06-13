from .models import Album,Track
from rest_framework import serializers

# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Album
#         fields = ['album_name','artist','tracks']


# class AlbumSerializer(serializers.ModelSerializer):
#     tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Album
#         fields = ['album_name', 'artist', 'tracks']


class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']