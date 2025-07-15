from django.contrib import admin
from .models import Student, Section, Year, Branch, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('s_roll', 's_fname', 's_lname', 's_branch', 's_year', 's_section')
    search_fields = ('s_roll', 's_fname', 's_lname')
    list_filter = ('s_branch', 's_year', 's_section')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('section',)

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('year',)

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('branch',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date')
    list_filter = ('date', 'student__s_branch')
    search_fields = ('student__s_roll', 'student__s_fname', 'student__s_lname')
