from django.urls import path, include
from rest_framework.routers import DefaultRouter


from comments.views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]