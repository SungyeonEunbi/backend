from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):

    def create_user(self, username, password):
        if not username:
            raise ValueError('User must have a username')
        
        user = self.model(
            username=username,
        )
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

    kakao = models.CharField(
        verbose_name='kakao',
        max_length=255,
        unique=True,
    )

    naver = models.CharField(
        verbose_name='naver',
        max_length=255,
        unique=True,
    )

    google = models.CharField(
        verbose_name='google',
        max_length=255,
        unique=True,
    )

    github = models.CharField(
        verbose_name='github',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin
