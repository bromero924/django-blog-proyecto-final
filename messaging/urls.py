from django.urls import path
from .views import inbox_view, send_message_view, message_detail_view

urlpatterns = [
    path('', inbox_view, name='inbox'),
    path('send/', send_message_view, name='send_message'),
    path('int:pk>/', message_detail_view, name='message_detail'),
]