from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from  .views import *


app_name = 'post_in'

urlpatterns = [
    path('notes/', notes_list),
    path('notes/<int:pk>/', notes_details),
]
urlpatterns = format_suffix_patterns(
    urlpatterns
)
