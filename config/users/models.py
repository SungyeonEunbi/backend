from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_jwt_user(self, username, password):
        if not username:
            raise ValueError('User must have a username')
        
        user = self.model(username=username)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_social_user(self, email, username, password):
        if not email:
            raise ValueError('Social login requires an email address')
        if not username:
            raise ValueError('Social login requires a username')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=True,
        null=True, 
    )

    kakao = models.CharField(
        verbose_name='kakao',
        max_length=255,
        blank=True,
        null=True,
    )

    naver = models.CharField(
        verbose_name='naver',
        max_length=255,
        blank=True,
        null=True,
    )

    google = models.CharField(
        verbose_name='google',
        max_length=255,
        blank=True,
        null=True,
    )

    github = models.CharField(
        verbose_name='github',
        max_length=255,
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  

    def __str__(self):
        return self.username 

    @property
    def is_staff(self):
        return self.is_admin
