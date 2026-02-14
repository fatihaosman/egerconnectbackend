from rest_framework.routers import DefaultRouter
from .views import NoticeViewSet, LostAndFoundViewSet, ScholarshipViewSet

router = DefaultRouter()
router.register("notices", NoticeViewSet)
router.register("lost-found", LostAndFoundViewSet)
router.register("scholarships", ScholarshipViewSet)

urlpatterns = router.urls
