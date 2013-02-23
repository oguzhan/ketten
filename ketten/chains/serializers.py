from rest_framework import serializers

from models import Chain, Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('date',)


class ChainSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True)

    class Meta:
        model = Chain
        fields = ('id', 'title', 'starting_date', 'links')  # TODO streaks
        read_only_fields = ('id',)
