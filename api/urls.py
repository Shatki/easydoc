"""easydoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework.authtoken import views
from .views import BankList, BankDetail, UserList, UserDetail, CounterpartList, CounterpartDetail
from .views import UserCreate, LoginView


urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("users/", UserList.as_view(), name="users_list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="users_detail"),
    path("users/create/", UserCreate.as_view(), name="user_create"),
    path("counterparts/", CounterpartList.as_view(), name="counterparts_list"),
    path("counterparts/<int:pk>/", CounterpartDetail.as_view(), name="counterparts_detail"),
    path("banks/", BankList.as_view(), name="banks_list"),
    path("banks/<int:pk>/", BankDetail.as_view(), name="banks_detail"),

    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/registration/account-confirm-email/', include('rest_auth.registration.urls')),
]
