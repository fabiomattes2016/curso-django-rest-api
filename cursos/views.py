from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import *
from .serializers import *


class CursoAPIView(APIView):
    def get(self, request: Request) -> Response:
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)

        return Response(serializer.data)
    
    
    def post(self, request: Request) -> Response:
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):
    def get(self, request: Request) -> Response:
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)

        return Response(serializer.data)
    

    def post(self, request: Request) -> Response:
        serializer = AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
