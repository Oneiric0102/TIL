from .views import TODOViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("TODO", TODOViewSet)

urlpatterns = router.urls
