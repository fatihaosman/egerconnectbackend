from rest_framework.routers import DefaultRouter
from .views import EventsViewSet, NoticeViewSet, LostAndFoundViewSet, ScholarshipViewSet

router = DefaultRouter()
router.register("notices", NoticeViewSet)
router.register("lost-found", LostAndFoundViewSet)
router.register("scholarships", ScholarshipViewSet)
router.register("events", EventsViewSet)

urlpatterns = router.urls
