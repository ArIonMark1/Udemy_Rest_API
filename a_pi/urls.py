from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from  .views import *
from rest_framework.routers import DefaultRouter

app_name = 'a_pi'

router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')
urlpatterns = router.urls

# notes_list = NoteViewSet.as_view({'get': 'list', 'post': 'create'})
# notes_detail = NoteViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# urlpatterns = [
#     # =======================================
#     # path('notes/', notes_list),
#     # path('notes/<int:pk>/', notes_details),
#     # =======================================
#     # path('notes/', NoteListView.as_view()),
#     # path('notes/<int:pk>/', NoteDetailView.as_view(), name='notes-detail'),
#     # =======================================
#     path('notes/', notes_list, name='notes_list'),
#     path('notes/<int:pk>', notes_detail, name='notes_detail'),
# ]
# urlpatterns = format_suffix_patterns(
#     urlpatterns
# )
