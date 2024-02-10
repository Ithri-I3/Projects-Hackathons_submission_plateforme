from django.contrib import admin
from .models import Challenge, Submission, Judge, Critic, Review

# Register your models here.


admin.site.register(Challenge)
admin.site.register(Submission)
admin.site.register(Judge)
admin.site.register(Critic)
admin.site.register(Review)
