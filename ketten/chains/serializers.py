from rest_framework import serializers

from chain.models import Chain


class ChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields = ('id', 'title', 'starting_date', 'links')  # TODO streaks
