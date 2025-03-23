# library_app/views.py
from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from .models import Book, Admin
from .serializers import BookSerializer, AdminSignupSerializer, AdminLoginSerializer

# API Views
class AdminSignupView(APIView):
    def post(self, request):
        serializer = AdminSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Admin created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminLoginView(APIView):
    def post(self, request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            admin = authenticate(
                request, 
                email=serializer.validated_data['email'], 
                password=serializer.validated_data['password']
            )
            if admin:
                token, created = Token.objects.get_or_create(user=admin)
                return Response({
                    'token': token.key,
                    'user_id': admin.pk,
                    'email': admin.email
                })
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

# Template Views for Web Interface
def admin_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password != password2:
            return render(request, 'library_app/admin_signup.html', {'error': 'Passwords do not match'})
        
        if Admin.objects.filter(email=email).exists():
            return render(request, 'library_app/admin_signup.html', {'error': 'Email already exists'})
        
        admin = Admin.objects.create_user(username=username, email=email, password=password)
        return redirect('admin_login')
    
    return render(request, 'library_app/admin_signup.html')

def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('book_list')
        else:
            return render(request, 'library_app/admin_login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'library_app/admin_login.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library_app/book_list.html', {'books': books})

def book_form(request, pk=None):
    book = None
    if pk:
        book = Book.objects.get(pk=pk)
    
    if request.method == 'POST':
        if book:
            # Update existing book
            book.title = request.POST.get('title')
            book.author = request.POST.get('author')
            book.isbn = request.POST.get('isbn')
            book.publication_year = request.POST.get('publication_year')
            book.publisher = request.POST.get('publisher')
            book.quantity = request.POST.get('quantity')
            book.save()
        else:
            # Create new book
            Book.objects.create(
                title=request.POST.get('title'),
                author=request.POST.get('author'),
                isbn=request.POST.get('isbn'),
                publication_year=request.POST.get('publication_year'),
                publisher=request.POST.get('publisher'),
                quantity=request.POST.get('quantity')
            )
        return redirect('book_list')
    
    return render(request, 'library_app/book_form.html', {'book': book})

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('book_list')

def student_view(request):
    books = Book.objects.all()
    return render(request, 'library_app/student_view.html', {'books': books})