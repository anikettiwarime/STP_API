from rest_framework import serializers
from curriculum.models import Standard, Subject, Lesson, WorkingDay, TimeSlot, SlotSubject, Comment, Reply, Event
from users.models import User, Feedback


class UserRegistrationSerializer(serializers.ModelSerializer):
    # We are writing this becoz we need confirm password field in our Registratin Request

    class Meta:
        model = User
        fields = ['email', 'name', 'password',]
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'is_active',
                  'is_staff', 'is_student', 'is_teacher', 'is_superuser']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user


# Feedback Serializer


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


# Curricullum App Serializer
class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    standard = StandardSerializer(many=False)

    class Meta:
        model = Subject
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    Standard = StandardSerializer(many=False)
    created_by = UserSerializer(many=False)
    subject = SubjectSerializer(many=False)

    class Meta:
        model = Lesson
        fields = '__all__'


class WorkingDaySerializer(serializers.ModelSerializer):
    standard = StandardSerializer(many=False)

    class Meta:
        model = WorkingDay
        fields = '__all__'


class TimeSlotSerializer(serializers.ModelSerializer):
    standard = StandardSerializer(many=False)

    class Meta:
        model = TimeSlot
        fields = '__all__'


class SlotSubjectSerializer(serializers.ModelSerializer):
    day = WorkingDaySerializer(many=False)
    standard = StandardSerializer(many=False)
    slot = TimeSlotSerializer(many=False)
    slot_subject = SubjectSerializer(many=False)

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
