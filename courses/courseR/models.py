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
    link = models.URLField(default='https://www.edx.org/?utm_source=google&utm_campaign=20875889732&utm_medium=cpc&utm_term=edx&hsa_acc=7245054034&hsa_cam=18736834479&hsa_grp=156544591323&hsa_ad=685047831561&hsa_src=g&hsa_tgt=kwd-89882436&hsa_kw=edx&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=CjwKCAjwgdayBhBQEiwAXhMxti3XfHTwk2dUXoYUukSnDJS7BephzuxrDTuLUR-tai4GGEeZVr9D3RoCmakQAvD_BwE')
    def __str__(self):
        return self.title
