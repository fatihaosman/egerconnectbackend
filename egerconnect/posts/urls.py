from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    EventsViewSet, NoticeViewSet, LostAndFoundViewSet,
    ScholarshipViewSet, SupportRequestViewSet,
    ClubViewSet,
    events_page, notices_page, lost_and_found_page,
    scholarships_page, support_request_page
)

router = DefaultRouter()
router.register("notices", NoticeViewSet)
router.register("lost-found", LostAndFoundViewSet)
router.register("scholarships", ScholarshipViewSet)
router.register("events", EventsViewSet)
router.register("support-requests", SupportRequestViewSet, basename="support-requests")
router.register("clubs", ClubViewSet, basename="clubs")  # ✅ ADD HERE

# Template routes (optional)
template_urls = [
    path("events-page/", events_page, name="events_page"),
    path("notices-page/", notices_page, name="notices_page"),
    path("lost-and-found-page/", lost_and_found_page, name="lost_and_found_page"),
    path("scholarships-page/", scholarships_page, name="scholarships_page"),
    path("support-request-page/", support_request_page, name="support_request_page"),
]

# ✅ COMBINE ONCE
urlpatterns = router.urls + template_urls