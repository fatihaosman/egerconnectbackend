
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# AbstractBaseUser → gives password handling, lastlogin,setpass and check passwords(basic authentication logic)

# PermissionsMixin → gives permissions & admin access

# USERNAME_FIELD → tells Django what field is used for login

# UserManager → controls how users are created


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)  # prevents duplicate email issues  due to capital letters

        user = self.model(email=email, **extra_fields)   #This creates a User object in memory.
        user.set_password(password)   # It hashes the password.
        user.save(using=self._db)    #saves user to the db
        return user
    
    
#WE CRRATE A  SUPER USER
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True) #If not specified, set is_staff=True.
        extra_fields.setdefault("is_superuser", True)   #Give full admin privileges.

        return self.create_user(email, password, **extra_fields)    #So superuser is just a special user.

#OUR USER MODEL FILEDS
class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)    #NO TWO users can register same email.
    registration_number = models.CharField(max_length=50)
    faculty_department = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    is_active = models.BooleanField(default=True)  #if true-user can login, if false-user is not allowed to login
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True) # useful for: sorting users out and tracking registrations.
 
    objects = UserManager()  # because we cretaed our own user then we need to tell django to use our user manager for creating users and superusers.

    USERNAME_FIELD = "email"  #“When someone logs in, treat email as username.”
    REQUIRED_FIELDS = ["full_name", "registration_number"]

    def __str__(self):
        return self.email

