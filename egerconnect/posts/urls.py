from rest_framework.routers import DefaultRouter
from .views import EventsViewSet, NoticeViewSet, LostAndFoundViewSet, ScholarshipViewSet, SupportRequestViewSet

router = DefaultRouter()
router.register("notices", NoticeViewSet)
router.register("lost-found", LostAndFoundViewSet)
router.register("scholarships", ScholarshipViewSet)
router.register("events", EventsViewSet)
router.register("support-requests", SupportRequestViewSet, basename="support-requests")


urlpatterns = router.urls
