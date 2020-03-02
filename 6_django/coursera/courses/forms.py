from django import forms

from courses.models import Lesson, Course
from users.models import Tutor, Student


class BlogBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CourseForm(BlogBaseForm):
    class Meta:
        model = Course
        fields = ['name', 'description']


class LessonForm(BlogBaseForm):
    class Meta:
        model = Lesson
        fields = ['name', 'date', 'description']
