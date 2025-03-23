# library_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    # API endpoints
    path('api/', include(router.urls)),
    path('api/admin/signup/', views.AdminSignupView.as_view(), name='api_admin_signup'),
    path('api/admin/login/', views.AdminLoginView.as_view(), name='api_admin_login'),
    
    # web interface
    path('signup/', views.admin_signup, name='admin_signup'),
    path('login/', views.admin_login, name='admin_login'),
    path('books/', views.book_list, name='book_list'),
    path('books/new/', views.book_form, name='new_book'),
    path('books/edit/<int:pk>/', views.book_form, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('student/', views.student_view, name='student_view'),
]