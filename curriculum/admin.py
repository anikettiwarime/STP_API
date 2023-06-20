from django.contrib import admin
from curriculum.models import Standard, Subject, Lesson, WorkingDay, TimeSlot, SlotSubject, Comment, Reply, Event

# Register your models here.
admin.site.register(Standard)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(WorkingDay)
admin.site.register(TimeSlot)
admin.site.register(SlotSubject)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Event)
