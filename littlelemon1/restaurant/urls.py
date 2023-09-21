#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('index', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]

