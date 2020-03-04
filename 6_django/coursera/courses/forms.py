from django import forms
from django.forms import inlineformset_factory

from courses.models import Course, Lesson


class BlogBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class LessonForm(BlogBaseForm):
    class Meta:
        model = Lesson
        exclude = ()


LessonFormSet = inlineformset_factory(Course, Lesson, form=LessonForm,
                                      fields=['date', 'name', 'description'],
                                      extra=1, can_delete=True)


class CourseForm(BlogBaseForm):
    class Meta:
        model = Course
        exclude = ()
