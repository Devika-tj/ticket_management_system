from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, pen_number, password=None, **extra_fields):
        if not pen_number:
            raise ValueError("PEN number is required")

        user = self.model(
            pen_number=pen_number,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, pen_number, password=None, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", "ADMIN")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            pen_number,
            password,
            **extra_fields
        )


class User(AbstractUser):

    ROLE_CHOICES = [
        ("STAFF", "Staff"),
        ("SUPPORT", "Support Staff"),
        ("ADMIN", "Admin"),
    ]

    username = None

    pen_number = models.CharField(
        max_length=7,
        unique=True
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="STAFF"
    )

    objects = UserManager()

    USERNAME_FIELD = "pen_number"

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    def __str__(self):
        return self.pen_number