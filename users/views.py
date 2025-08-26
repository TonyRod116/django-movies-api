from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.common import AuthSerializer

# Create your views here.
class SignupView(APIView):
  def post(self, request):
    serialized_user = AuthSerializer(data=request.data)
    if serialized_user.is_valid(raise_exception=True):
      serialized_user.save()
    return Response(serialized_user.data, 201)


class SignInView(APIView):
  def post(self, request):
    # print(request.data)
    return Response({"message": "HIT LOGIN ROUTE"})