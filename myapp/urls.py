from rest_framework import routers
from .views import CustomUserViewSet, RoleViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'items', ItemViewSet)

urlpatterns = router.urls
