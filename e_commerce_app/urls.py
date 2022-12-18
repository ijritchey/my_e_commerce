from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('items/', views.items_index, name='items_index'),
    path('category/', views.categorys_index, name='category_index'),
    path('category/<int:category_id>', views.categorys_show, name='category_show'),
    path('items/<int:item_id>/', views.items_show, name='items_show'),
    path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    path('items/<int:pk>/update', views.ItemUpdate.as_view(), name='items_update'),
    path('items/<int:pk>/delete', views.ItemDelete.as_view(), name='items_delete'),
    path('user/<username>', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('accounts/login/', views.login_view, name='require_login')
]
