from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('items/', views.items_index, name='items_index'),
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('items/<int:pk>/update', views.ItemUpdate.as_view(), name='itmes_update'),
    path('items/<int:pk>/delete', views.ItemDelete.as_view(), name='itmes_delete'),
    path('user/<username>', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('accounts/login/', views.login_view, name='require_login')
]
