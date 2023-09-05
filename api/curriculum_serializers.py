# Curriculum App Serializer
from rest_framework import serializers

from api.auth_serializers import UserSerializer
from curriculum.models import Standard, Subject, Lesson, WorkingDay, TimeSlot, SlotSubject, Comment, Reply, Event, Feedback


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    # standard = StandardSerializer(many=False)

    class Meta:
        model = Subject
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    # Standard = StandardSerializer(many=False)
    # created_by = UserSerializer(many=False)
    # subject = SubjectSerializer(many=False)

    class Meta:
        model = Lesson
        fields = '__all__'


class WorkingDaySerializer(serializers.ModelSerializer):
    # standard = StandardSerializer(many=False)

    class Meta:
        model = WorkingDay
        fields = '__all__'


class TimeSlotSerializer(serializers.ModelSerializer):
    # standard = StandardSerializer(many=False)

    class Meta:
        model = TimeSlot
        fields = '__all__'


class SlotSubjectSerializer(serializers.ModelSerializer):
    # day = WorkingDaySerializer(many=False)
    # standard = StandardSerializer(many=False)
    # slot = TimeSlotSerializer(many=False)
    # slot_subject = SubjectSerializer(many=False)

    class Meta:
        model = SlotSubject
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
