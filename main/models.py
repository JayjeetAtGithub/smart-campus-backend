from django.db import models
<<<<<<< HEAD
from django.contrib.auth import models as auth_models


class User(auth_models.User):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_cr = models.BooleanField(default=False)
    roll_no = models.CharField(max_length=10)

    def __str__(self):
        return self.roll_no

=======
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given username
        and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        #always normalize username
        user = self.model(
            username=self.model.normalize_username(username),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        """
        Creates and saves a staffuser with the given username 
        and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using = self._db)
        return user


    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username 
        and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(blank = True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    roll_no = models.CharField(max_length=16, unique=True, blank=True, null=True)

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    student = models.BooleanField(default=False)
    cr = models.BooleanField(default=False)
    faculty = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] #USERNAME_FIELD and password are required by default
    
    objects = UserManager()


    def __str__(self):
        return self.username


    # get_full_name and get_short_name are not required in Django2.0
    def has_perm(self, perm , obj = None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True


    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_faculty(self):
        return self.faculty

    @property
    def is_cr(self):
        return self.cr

    @property
    def is_student(self):
        return self.student
        
    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
>>>>>>> f1590b6c9684816d6f5d26fe5e5e46f042504245
