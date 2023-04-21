from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.template.defaultfilters import slugify
from django.db import models
from django.urls import reverse
import qrcode

# Create your models here.
class User(AbstractUser):
    class Gender(models.IntegerChoices):
        MALE = 0
        FEMALE = 1

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.IntegerField(choices=Gender.choices, default=0)
    profile_img = models.ImageField(null=True, default="default_pfp.jpg")
    qr_code = models.ImageField(null=True)
    slug = models.SlugField(null=False, unique=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'birthdate', 'gender']

    def save(self, *args, **kwargs):
        if not self.pk:
            qr_img = qrcode.make(self.username)
            qr_path = self.username + ".png"
            qr_img.save("media/" + qr_path)
            self.qr_code = qr_path

        self.slug = slugify(self.username)
        return super().save(*args, **kwargs)