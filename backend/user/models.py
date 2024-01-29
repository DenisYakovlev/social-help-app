import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class AnonUserManager(BaseUserManager):
    def create_user(self, id, **extra_fields):
        if not id:
            raise ValueError(_("Id is required"))
        
        user = self.model(id=id, **extra_fields)
        user.save()
        return user

    def create_superuser(self, id, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        
        user = self.model(id=id, **extra_fields)
        user.set_password(password)
        user.save()

        return user


# Create your models here.


class AnonUser(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=256, primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(max_length=256, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    is_superuser = models.BooleanField(
        _("superuser status"),
        default=False,
        help_text=_(
            "Designates that this user has all permissions without "
            "explicitly assigning them."
        ),
    )

    objects = AnonUserManager()
    USERNAME_FIELD = 'id'
