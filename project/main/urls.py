from django.urls import path
from . import views
app_name = "app_vladislav_yurenya"

urlpatterns = [
    path('', views.ListPost.as_view(), name = "all_post"),
    path('create_post/', views.CreatePost.as_view(), name="create_post"),
    path('post/<int:pk>/detail', views.DetailPost.as_view(), name="detail"),
    path('post/<int:pk>/update', views.UpdatePost.as_view(), name="update"),
    path('post/<int:pk>/delete', views.DeletePost.as_view(), name="delete"),
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('enter/', views.EnterUser.as_view(), name='enter'),
    path('profile/', views.DetailProfile.as_view(), name='profile'),
    path('update_profile/<int:pk>/', views.UpdateProfile.as_view(), name='update_profile'),
    path('my_post/', views.MyPostList.as_view(), name='my_post_list'),
    path('my_post/<int:pk>/update', views.MyPostUpdate.as_view(), name='my_post_update'),
    path('my_post/<int:pk>/delete', views.MyPostDelete.as_view(), name='my_post_delete'),
    path('filter_tag_post/', views.FilterTag.as_view(), name='filter_tag_post'),


]
