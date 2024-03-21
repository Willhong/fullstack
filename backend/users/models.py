from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group
from django.db import models


def create_default_groups(sender, **kwargs):
    group_names = ["MasterAdmin", "사장", "영업진", "웨이터", "호스티스"]
    for group_name in group_names:
        Group.objects.get_or_create(name=group_name)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


def get_default_group():
    group, created = Group.objects.get_or_create(name='호스티스')
    return group.id


class User(AbstractBaseUser, PermissionsMixin):
    idx = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    store = models.ForeignKey(
        'stores.Store', on_delete=models.DO_NOTHING, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'groups']

    groups = models.ForeignKey(
        'auth.Group',
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set",
        related_query_name="user",
        on_delete=models.DO_NOTHING,
        default=get_default_group
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.email

    def get_group(self):
        """사용자가 속한 그룹 이름을 반환합니다."""
        groups = self.groups.all()
        return ', '.join(group.name for group in groups) if groups else 'No Group'
