from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('get-books/', views.get_books_by_mood, name='get_books'),
    path('favorite/<int:book_id>/', views.add_favorite, name='add_favorite'),
    path('favorites/', views.list_favorites, name='favorites'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),

    # 🔧 New placeholder pages
    path('explore/', views.explore_view, name='explore'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('profile/', views.profile_view, name='profile'),

    path('favorites/', views.favorites_view, name='favorites'),
    path('favorites/list/', views.list_favorites, name='list_favorites'),
    path('favorites/add/<int:book_id>/', views.add_favorite, name='add_favorite'),
    path('favorites/remove/<int:book_id>/', views.remove_favorite, name='remove_favorite'),
]
