from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookViewSet, LibraryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'libraries', LibraryViewSet)

urlpatterns = router.urls