from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from models import Chain
from serializers import ChainSerializer


class ChainList(APIView):
    """
    View for Chains collection of a specified user.
    """
    # TODO authentication wrapper
    def get(self, request, format=None):
        chains = Chain.objects.all()  # TODO replace .all with user's chains
        serializer = ChainSerializer(chains, many=True)
        return Response(serializer.data)

    # TODO authentication wrapper
    def post(self, request, format=None):
        serializer = ChainSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChainDetail(APIView):
    """
    View for chain resource details.
    """
    def get_object(self, pk):
        try:
            return Chain.objects.get(pk=pk)
        except Chain.DoesNotExist:
            raise Http404

    # TODO authentication wrapper
    def get(self, request, pk, format=None):
        chain = self.get_object(pk)
        serializer = ChainSerializer(chain)
        return Response(serializer.data)

    # TODO authentication wrapper
    def put(self, request, pk, format=None):
        chain = self.get_object(pk)
        serializer = ChainSerializer(chain, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # TODO authentication wrapper
    def delete(self, request, pk, format=None):
        chain = self.get_object(pk)
        chain.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
