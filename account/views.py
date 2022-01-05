from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class LoginView(APIView):
    def post(self,request):
        user = authenticate(request,username=request.data.get('username'),password=request.data.get('password'))
        if user is None:
            return Response({"error": "Login va/yoki parol xato"})

        token,create = Token.objects.get_or_create(user=user)

        return Response({
            'token' : token.key,
            'user':UserSerializer(user).data
        })

class MeView(APIView):
    permission_classes = (IsAuthenticated, )
    def get(self,request):
        return Response({
            "is_authenticated":request.user.is_authenticated,
            "user":UserSerializer(request.user).data if request.user.is_authenticated else None
        })
    def delete(self, request):
        request.auth.delete()

        return Response({
            "ok":True
        })
