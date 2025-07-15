from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator, MaxValueValidator

class Section(models.Model):
    section = models.CharField(max_length=2)

    def __str__(self):
        return self.section

class Year(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    def __str__(self):
        return str(self.year)

class Branch(models.Model):
    branch = models.CharField(max_length=10)

    def __str__(self):
        return self.branch

class Student(models.Model):
    s_roll = models.CharField(max_length=20, primary_key=True)
    s_fname = models.CharField(max_length=20)
    s_lname = models.CharField(max_length=20)
    s_branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    s_section = models.ForeignKey(Section, on_delete=models.CASCADE)
    s_year = models.ForeignKey(Year, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.s_fname} {self.s_lname} - {self.s_roll}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=now)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'date'], name='unique_attendance_per_day')
        ]

    def __str__(self):
        return f"{self.student.s_roll} - {self.date}"
