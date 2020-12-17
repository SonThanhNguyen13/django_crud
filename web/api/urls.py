from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('token/', obtain_auth_token, name='get_token'),
    path('', views.Index.as_view(), name='welcome'),
    path('data/list/', views.DataList.as_view(), name='list_data'),
    path('data/detail/<int:pk>/', views.DataDetail.as_view(), name='detail'),
]
