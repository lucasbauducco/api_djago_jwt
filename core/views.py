# core/views.py
# core/views.py
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import UserRole, Scope, Category, Subcategory, Calendar, MissingPet, ContactType, Contact
from .serializers import (
    UserSerializer,
    UserRoleSerializer,
    ScopeSerializer,
    CategorySerializer,
    SubcategorySerializer,
    CalendarSerializer,
    MissingPetSerializer,
    ContactTypeSerializer,
    ContactSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

class ScopeViewSet(viewsets.ModelViewSet):
    queryset = Scope.objects.all()
    serializer_class = ScopeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

class MissingPetViewSet(viewsets.ModelViewSet):
    queryset = MissingPet.objects.all()
    serializer_class = MissingPetSerializer

class ContactTypeViewSet(viewsets.ModelViewSet):
    queryset = ContactType.objects.all()
    serializer_class = ContactTypeSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
