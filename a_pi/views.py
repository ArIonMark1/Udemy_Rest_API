from django.shortcuts import render
from rest_framework.decorators import api_view
from notes.models import Note
from rest_framework.response import Response
from rest_framework import status
from .serializers import ThinNoteSerializer, NoteSerializer
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, \
    UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


# Create your views here.
# ======================= ViewSets =======================

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = IsAuthenticated, # добавление проверки на авторизацию на сайте
    # http_method_names = ['get', 'put', 'post', 'delete']

    def list(self, request, *args, **kwargs):
        # notes = Note.objects.all()
        notes = Note.objects.filter(author=self.request.user) # отображение записей текущего пользователя
        context = {'request': request}
        serializer = ThinNoteSerializer(notes, many=True, context=context)
        return Response(serializer.data)

    def perform_create(self, serializer): # подвязывание под юзера
        serializer.save(author=self.request.user)

# =======================================================
# ===================== Serializers =====================
# class NoteListView(ListCreateAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#
#     def list(self, request, *args, **kwargs):
#         """ Переопределяем сериализатор """
#         notes = Note.objects.all()
#         context = {'request': request}
#         serializer = ThinNoteSerializer(notes, many=True, context=context)
#         return Response(serializer.data)
#
# class NoteDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer


# ==================== V2 ====================
# class NoteListView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     """ Получение списка обьектов с помощью миксинов """
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#
#     def get(self, request, *args, **kwargs):
#         self.serializer_class = ThinNoteSerializer
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# ==================== V1 mixin ======================
# class NoteDetailView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
#     """ Редактирование, удаление обьектов с помощью миксинов """
#     queryset = Note.objects.all()
#     serializer_class = NoteSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class NoteListView(APIView):
#     def get(self, request, format=None):
#         notes = Note.objects.all()
#         context = {'request': request}
#         serializer = ThinNoteSerializer(notes, many=True, context=context)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ===============================================================================
# ================================= CBV version =================================

# class NoteDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             return Note.objects.get(pk=pk)
#         except Note.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk, format=None):
#
#         notes = self.get_object(pk)
#         print(notes)
#         serializer = NoteSerializer(notes)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         notes = self.get_object(pk)
#         serializer = NoteSerializer(notes, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         notes = self.get_object(pk)
#         notes.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ==========================================================
# ================== functional (FBV) version ====================
#
#
# @api_view(['GET', 'POST'])
# def notes_list(request, format=None):
#     if request.method == 'GET':
#         notes = Note.objects.all()
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# ==============================================================================

# @api_view(['GET', 'PUT', 'DELETE'])
# def notes_details(request, pk, format=None):
#     try:
#         note = Note.objects.get(pk=pk)
#     except Note.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':  # получение данных
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)
#     elif request.method == 'PUT':  # редактирование данных
#         serializer = NoteSerializer(note, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         note.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
