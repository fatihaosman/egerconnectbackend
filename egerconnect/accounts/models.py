
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# AbstractBaseUser → gives password handling

# PermissionsMixin → gives permissions & admin access

# USERNAME_FIELD → tells Django what field is used for login

# UserManager → controls how users are created


class UserManager(BaseUserManager):
    def create_user(self, registration_number, password=None, **extra_fields):
        if not registration_number:
            raise ValueError("Registration number is required")

        user = self.model(
            registration_number=registration_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, registration_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(registration_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    faculty_department = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "registration_number"
    REQUIRED_FIELDS = ["full_name", "email"]

    def __str__(self):
        return self.registration_number
