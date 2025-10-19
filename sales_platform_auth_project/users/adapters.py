# users/adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        """
        Цей метод викликається після успішного входу через соцмережу.
        Він заповнює поля нашої CustomUser моделі даними з провайдера.
        """
        user = super().populate_user(request, sociallogin, data)

        # Перевіряємо, чи є дані від провайдера
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        picture_url = data.get('picture')

        # Заповнюємо поля користувача
        if first_name and not user.first_name:
            user.first_name = first_name

        if last_name and not user.last_name:
            user.last_name = last_name

        if picture_url and not user.profile_picture_url:
            user.profile_picture_url = picture_url

        if email and not user.email:
            user.email = email

        # ЗБЕРІГАЄМО ЗМІНИ В БАЗУ ДАНИХ!
        #user.save()

        return user