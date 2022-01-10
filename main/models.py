from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.template.defaultfilters import slugify
from secrets import token_hex

class MemberManager(BaseUserManager):
    def create_user(
        self, first_name, last_name, email, password, mobile_number, address, country, gender, **other_fields
    ):
        other_fields.setdefault("is_staff", False)
        other_fields.setdefault("is_superuser", False)
        other_fields.setdefault("is_active", True)

        if not email:
            raise ValueError("Please provide a email address.")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=self.normalize_email(email),
            email=self.normalize_email(email),
            mobile_number=mobile_number,
            address=address,
            country=country,
            gender=gender,
            **other_fields
        )
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, first_name, last_name, email, password, mobile_number, address, country, gender, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        return self.create_user(first_name, last_name, email, password, mobile_number, address, country, gender, **other_fields)


class Member(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.CharField(max_length=80, unique=True)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=80)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    mobile_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MemberManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "mobile_number", "address", "country", "gender"]

    def __str__(self):
        return f"{self.id}-{self.email}"


class YachtType(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(YachtType, self).save(*args, **kwargs)


def get_image_filename(instance, filename):
    return "images/%s-%s" % (token_hex(10), filename)

class Yacht(models.Model):
    name = models.CharField(max_length=80)
    rate = models.IntegerField()
    capacity = models.IntegerField()
    yacht_type = models.ForeignKey(YachtType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Yacht - {self.name}"

class YachtBooking(models.Model):
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Yacht - {self.name}"

class Event(models.Model):
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    slug = models.SlugField()
    days = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Event - {self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Event, self).save(*args, **kwargs)

class EventBooking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"EventBooking - {self.event.name} - {self.member.email}"

class Training(models.Model):
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    slug = models.SlugField()
    days = models.IntegerField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Training - {self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Training, self).save(*args, **kwargs)


class TrainingBooking(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"EventBooking - {self.training.name} - {self.member.email}"    


class Package(models.Model):
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    slug = models.SlugField()
    price = models.IntegerField()
    days = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to=get_image_filename, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Package: {self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Package, self).save(*args, **kwargs)

class PackageBooking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PackageBooking - {self.package.name} - {self.member.email}"


class Employee(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.CharField(max_length=80, unique=True)
    address = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=80)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    mobile_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=80)
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Employee - {self.email}"

class Feedback(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.CharField(max_length=80, unique=True)
    mobile_number = models.CharField(max_length=20)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Feedback - {self.email}"
