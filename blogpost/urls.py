from django.urls import path
from .views import BlogList, BlogDetail, BlogCreate, BlogDelete

urlpatterns = [
    path('list/', BlogList.as_view(), name='list'),
    path('detail/<int:pk>', BlogDetail.as_view()),
    path('create/', BlogCreate.as_view(), name='create'),
    path('delete/<int:pk>', BlogDelete.as_view(), name='delete'),
]
