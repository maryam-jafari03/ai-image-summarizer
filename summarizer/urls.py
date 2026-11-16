from rest_framework.routers import DefaultRouter
from summarizer.views import PhotoViewSet

router = DefaultRouter()
router.register('/photo', PhotoViewSet)

urlpatterns = router.urls