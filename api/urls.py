from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from .import views


urlpatterns = [
    path('kinopoisk-movies/<str:title>/', views.get_kinopoisk_movies),
    path('kinopoisk-movie/<str:kinopoisk_id>/', views.get_kinopoisk_movie),

    path('feed/', views.MovieListView.as_view()),
    path('movie/<str:pk>/', views.movie_view),
    path('add-movie/', views.AddMovieView.as_view()),
    path('profiles/', views.ProfileListView.as_view()),
    path('profile/<str:pk>/', views.profile_view),
    path('profile-feed/<str:pk>/', views.ProfileFeedListView.as_view()),
    path('notifications/<str:pk>/', views.NotificationListView.as_view()),
    path('notification/<str:pk>/', views.NotificationView.as_view()),
    path('active-chats/<str:pk>/', views.ActiveChatsListView.as_view()),
    path('chat/<str:user_id>/<str:recipient_id>/', views.ChatListView.as_view()),
    path('like/<str:movie_id>/', views.like_view),
    path('follow/<str:profile_id>/', views.follow_view),
    path('message/<str:recipient_id>/', views.message_view),
    path('comment/<str:movie_id>/', views.comment_view),

    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('logout/', views.LogoutView.as_view()),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
