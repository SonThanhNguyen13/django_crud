from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('token/', obtain_auth_token, name='get_token'),
    path('', views.Index.as_view(), name='welcome'),
    path('data/list/', views.DataList.as_view(), name='list_data'),
    path('data/search/<str:pk>/', views.SearchData.as_view(), name='search'),
    path('data/update', views.UpdateData.as_view(), name='update'),
    path('data/create', views.CreateData.as_view()),
    path('data/delete/<str:pk>', views.Delete.as_view()),

]
