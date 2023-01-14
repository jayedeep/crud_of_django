from django.urls import path
from .views import (HomeView,UserDeleteView,login_request
,logout_request,register_request,UpdateTemplateView)

urlpatterns = [
    path('delete/<int:id>',UserDeleteView.as_view(),name='delete'),
    path('update/<int:id>',UpdateTemplateView.as_view(),name='update'),

    path('',HomeView.as_view(),name='home'),

    path('login',login_request,name='login'),
    path('register',register_request,name='register'),
    path('logout',logout_request,name='logout'),

]
