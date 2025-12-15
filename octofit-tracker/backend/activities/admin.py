from django.contrib import admin
from .models import Activity, Workout

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'duration', 'points', 'date']
    list_filter = ['activity_type', 'date']
    search_fields = ['user__username', 'notes']

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'duration', 'created_at']
    search_fields = ['user__username', 'name']
