import uuid
from decouple import config

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from cloudinary.models import CloudinaryField
from auth_users.models import User


# Create your models here.
class Standard(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    standard = models.ForeignKey(
        Standard, on_delete=models.CASCADE, related_name='subjects')
    image = models.ImageField(
        upload_to='resources/subjects/', blank=False, verbose_name='Subject Image')
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Lesson(models.Model):
    # lesson_id = models.CharField(max_length=100, unique=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    Standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=250)
    position = models.PositiveSmallIntegerField(verbose_name="Chapter no.")
    slug = models.SlugField(null=True, blank=True)
    video = models.FileField(upload_to='lessons/videos/',
                             verbose_name="Video", blank=True, null=True)
    ppt = models.FileField(upload_to='lessons/ppt/',
                           verbose_name="Presentations", blank=True)
    Notes = models.FileField(upload_to='lessons/notes/',
                             verbose_name="Notes", blank=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('curriculum:lesson_list', kwargs={'slug': self.subject.slug, 'standard': self.Standard.slug})


class WorkingDay(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    standard = models.ForeignKey(
        Standard, on_delete=models.CASCADE, related_name='standard_days')
    day = models.CharField(max_length=100)

    def __str__(self):
        return self.day


class TimeSlot(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    standard = models.ForeignKey(
        Standard, on_delete=models.CASCADE, related_name='standard_time_slots')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time) + ' - ' + str(self.end_time)


class SlotSubject(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    standard = models.ForeignKey(
        Standard, on_delete=models.CASCADE, related_name='standard_slots')
    day = models.ForeignKey(
        WorkingDay, on_delete=models.CASCADE, related_name='standard_slots_days')
    slot = models.ForeignKey(
        TimeSlot, on_delete=models.CASCADE, related_name='standard_slots_time')
    slot_subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='standard_slots_subject')

    def __str__(self):
        return str(self.standard) + ' - ' + str(self.day) + ' - ' + str(self.slot) + ' - ' + str(self.slot_subject)


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    lesson_name = models.ForeignKey(
        Lesson, null=True, on_delete=models.CASCADE, related_name='lesson_comments')
    comm_name = models.CharField(max_length=100, blank=True)
    # reply = models.ForeignKey("Comment", null=True, blank=True, on_delete=models.CASCADE,related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comm_name = slugify(
            "comment by" + "-" + str(self.author) + str(self.date_added))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comm_name

    class Meta:
        ordering = ['-date_added']


class Reply(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    comment_name = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies')
    reply_body = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to " + str(self.comment_name.comm_name)


class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)
    Ondate = models.DateField()
    posted_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField("image")
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.description

    @property
    def image_url(self):
        return (
            f"https://res.cloudinary.com/{config('CLOUDINARY_CLOUD_NAME')}/{self.image}"
        )


# FeedBack :  name email feedback
class Feedback(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name
