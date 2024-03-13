from rest_framework import viewsets, generics, filters  
from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer,MatriculaSerializer,ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from django_filters.rest_framework import DjangoFilterBackend

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    #serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']
    def get_serializer_class(self):
        if self.request.version == 'v2': #rota: http://127.0.0.1:8000/estudantes/?version=v2
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']) #Primary Key
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculasCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk']) #Primary Key
        return queryset
    serializer_class = ListaMatriculasCursoSerializer