# core/urls.py
from django.urls import path, include
from rest_framework import routers
from .views import (
    UserViewSet, UserRoleViewSet, ScopeViewSet, CategoryViewSet, SubcategoryViewSet,
    CalendarViewSet, MissingPetViewSet, ContactTypeViewSet, ContactViewSet
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-roles', UserRoleViewSet)
router.register(r'scopes', ScopeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'calendars', CalendarViewSet)
router.register(r'missing-pets', MissingPetViewSet)
router.register(r'contact-types', ContactTypeViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
