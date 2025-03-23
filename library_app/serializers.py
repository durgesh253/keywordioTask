# library_app/serializers.py
from rest_framework import serializers
from .models import Admin, Book
from django.contrib.auth.password_validation import validate_password

class AdminSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Admin
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        admin = Admin.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        admin.set_password(validated_data['password'])
        admin.save()
        return admin

class AdminLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'