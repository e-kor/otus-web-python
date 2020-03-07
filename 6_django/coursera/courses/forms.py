from django import forms
from django.forms import inlineformset_factory
from courses.tasks import send_contact_mail
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


class ContactForm(forms.Form):
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        send_contact_mail.send(self.cleaned_data['email'], self.cleaned_data['body'])
