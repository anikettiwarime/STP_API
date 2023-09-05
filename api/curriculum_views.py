from rest_framework import viewsets
from curriculum.models import *
from .curriculum_serializers import *

from rest_framework.permissions import IsAuthenticated


class StandardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class WorkingDayViewSet(viewsets.ModelViewSet):
    queryset = WorkingDay.objects.all()
    serializer_class = WorkingDaySerializer


class TimeSlotViewSet(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer


class SlotSubjectViewSet(viewsets.ModelViewSet):
    queryset = SlotSubject.objects.all()
    serializer_class = SlotSubjectSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class FeedBackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     return Feedback.objects.filter(user=user)
