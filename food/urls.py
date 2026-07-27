from django.urls import path
from .views import food_list, category_list, RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import OrderCreateView
from .views import PlaceOrderView
from .views import OrderListCreateView
from .views import ProfileView
from .views import DashboardView

urlpatterns = [
    path('foods/', food_list),
    path('categories/', category_list),

    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    
    path('orders/', OrderListCreateView.as_view()),
    path("place-order/", PlaceOrderView.as_view()),
    path("create-order/", OrderCreateView.as_view()),
    path("profile/", ProfileView.as_view()),
    path("dashboard/",DashboardView.as_view()),
    
]