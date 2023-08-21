from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .auth_views import MyTokenObtainPairView, RegistrationView
from .curriculum_views import *

router = DefaultRouter()
router.register(r'standards', StandardViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'working-days', WorkingDayViewSet)
router.register(r'time-slots', TimeSlotViewSet)
router.register(r'slot-subjects', SlotSubjectViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'replies', ReplyViewSet)
router.register(r'events', EventViewSet)
router.register(r'feedbacks', FeedBackViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegistrationView.as_view(), name='register'),
]
