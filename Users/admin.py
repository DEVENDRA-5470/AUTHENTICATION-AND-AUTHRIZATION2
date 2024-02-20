from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','title','video', 'instructor', 'start_date', 'duration_in_weeks', 'created_at', 'updated_at')
    search_fields = ('title', 'instructor')
    list_filter = ('instructor', 'start_date')