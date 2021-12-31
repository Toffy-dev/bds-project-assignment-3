
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from phonenumber_field.modelfields import PhoneNumberField


class MyCustomerManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    phone_number = PhoneNumberField(region='CZ')
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    balance = models.PositiveIntegerField(null=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyCustomerManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class MyEmployeeManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    salary = models.IntegerField()

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_name'

    objects = MyEmployeeManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Customer_type(models.Model):
	customer_type = models.CharField(max_length=20)

class Customer_has_type(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_type = models.ForeignKey(Customer_type, on_delete=models.CASCADE)

class Address(models.Model):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    house_number = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=30)

class Customer_has_address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Order_menu(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

class Order_type(models.Model):
    order_type = models.CharField(max_length=30)

class Order_has_type(models.Model):
    order_menu = models.ForeignKey(Order_menu, on_delete=models.CASCADE)
    order_type = models.ForeignKey(Order_type, on_delete=models.CASCADE)

class Product_type(models.Model):
    product_type = models.CharField(max_length=30)

class Order_has_product(models.Model):
    order_menu = models.ForeignKey(Order_menu, on_delete=models.CASCADE)
    product_type = models.ForeignKey(Product_type, on_delete=models.CASCADE)

class Drink_type(models.Model):
    drink_type = models.CharField(max_length=30)

class Order_has_drink(models.Model):
    order_menu = models.ForeignKey(Order_menu, on_delete=models.CASCADE)
    drink_type = models.ForeignKey(Drink_type, on_delete=models.CASCADE)

class Employee_manages_order(models.Model):
    order_menu = models.ForeignKey(Order_menu, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
