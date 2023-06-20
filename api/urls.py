from django.urls import path, include
from rest_framework import routers
from .views import UserRegistrationView, UserLoginView, UserListViewSet, UserViewSet, FeedbackViewSet, StandardViewSet, SubjectViewSet, LessonViewSet, WorkingDayViewSet, TimeSlotViewSet, SlotSubjectViewSet, CommentViewSet, ReplyViewSet, EventViewSet

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# urlpatterns = [
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
# ]

router = routers.DefaultRouter()
router.register(r'regiter',UserRegistrationView,basename='registration')
router.register(r'users', UserListViewSet, basename="users")
router.register(r'user', UserViewSet, basename="user")
router.register(r'feedbacks', FeedbackViewSet, basename='feedbacks')
router.register(r'standards', StandardViewSet, basename='standards')
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'workingday', WorkingDayViewSet, basename='workingday')
router.register(r'timeslot', TimeSlotViewSet, basename='timeslot')
router.register(r'slotsubject', SlotSubjectViewSet, basename='slotsubject')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'reply', ReplyViewSet, basename='reply')
router.register(r'event', EventViewSet, basename='event')

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path("register/", UserRegistrationView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("", include(router.urls)),
]
