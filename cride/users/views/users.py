
#Django rest framework
from rest_framework.views import APIView
from rest_framework import status

# Serializers
from cride.users.serializers import UserLoginSerializer

class UserLoginAPIView(APIView):
    """User login api view."""
    def post(self,request, *args, **kwargs):
        serializer = UserLoginAPIView(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        data = {
            'status': 'ok',
            'token': token
        }
        return Res