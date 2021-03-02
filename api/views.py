from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api import serializers


class HelloApiView(APIView):
    """Test View Api"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, fromat=None):
        """Return list of API view feature """

        an_apiview = [
            'Hello My name is janmesh',
            'My hobbies are playing to marbles',
            'I am belongs to vadodara city',
            'I am a student',
            'I am studying in GCET college'
        ]

        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self, request):
        """ create hello message to our name """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message= f'Hello {name}'

            return Response({'message' : message})
        else :
            return Response(
                serializer.errors, 
                status= status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """ handling Update Object """

        return Response({'message' : 'PUT'})
        
    def patch(self, request, pk=None):
        """ Handling partial Object """

        return Response({'message' : 'PATCH'})

    def delete(self, request, pk=None):
        """ Deleting an Object """

        return Response({'message' : 'DELETE'})