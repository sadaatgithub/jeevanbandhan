from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('facebook', views.facebook, name='facebook'),
    path('help', views.help, name='help'),
    path('contact', views.contact, name='contact'),
    path('sign_up', views.sign_up, name='signup'),
    path('user_login',views.user_login, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('home', views.home, name='home'),
    path('search', views.search, name='search'),
    path('adv_search', views.adv_search, name='adv_search'),
    path('view_profile', views.view_profile, name='profile_detail'),
    path('view_self_profile', views.view_self_profile, name='self_profile_detail'),
    path('add_favourite', views.add_favourite, name='add_favourite'),
    path('search_by_id', views.search_by_id, name='search_by_id'),
    path('fav_list', views.fav_list, name='fav_list'),
    path("chatroom", views.chatroom, name="chatroom"),
    path("ajax/<int:pk>/", views.ajax_load_messages, name="chatroom-ajax"),


    # path('contactUs', views.contactUs, name='contactUs'),
]
