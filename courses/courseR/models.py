from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # Add your custom fields here if you have any
    # For example: additional_field = models.CharField(max_length=100)

    # Override the groups field with a unique related_name
    groups = models.ManyToManyField(
        Group,
        related_name='courseR_user_groups',  # Ensure this related_name is unique
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='user',
    )

    # Override the user_permissions field with a unique related_name
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='courseR_user_permissions',  # Ensure this related_name is unique
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.TextField()
    duration = models.TextField()
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)

    def __str__(self):
        return self.title
