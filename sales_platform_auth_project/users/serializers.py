# users/serializers.py
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True
    )
    # Явно вказуємо, що full_name - це поле тільки для читання (з моделі)
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        # Вказуємо всі поля для входу та виходу
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2',
            'full_name', # Додаємо full_name сюди
        )
        # Налаштовуємо, які поля є тільки для запису (не показувати у відповіді)
        extra_kwargs = {
            'password': {'write_only': True},
            'password2': {'write_only': True},
            'email': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        # Використовуємо вбудований метод, який правильно обробляє всі поля
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    """
    Серіалізатор для відображення повної інформації про користувача.
    """
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User  # get_user_model() посилається на вашу CustomUser
        fields = (
            'pk',
            'email',
            'username',
            'first_name',
            'last_name',
            'full_name',
            'profile_picture_url'
        )
        read_only_fields = fields