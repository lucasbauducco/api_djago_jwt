from django.db import models
from django.contrib.auth.models import User

# User roles
class UserRole(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Scope (local, provincial, national, international)
class Scope(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Event categories
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Event subcategories
class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return f"{self.category.name} - {self.name}"

# Calendar (events)
class Calendar(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=[('event', 'Event'), ('missing_pet', 'Missing Pet')])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calendars')
    scope = models.ForeignKey(Scope, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    photo = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Missing pets
class MissingPet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='missing_pets')
    scope = models.ForeignKey(Scope, on_delete=models.SET_NULL, null=True)
    last_seen = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('missing', 'Missing'), ('found', 'Found')], default='missing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Contact types
class ContactType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Contacts of the user who posts a missing pet or event
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    contact_type = models.ForeignKey(ContactType, on_delete=models.SET_NULL, null=True)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.contact_type.name} - {self.value}"
