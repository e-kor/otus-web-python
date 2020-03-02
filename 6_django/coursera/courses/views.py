from django.contrib.auth.decorators import user_passes_test, login_required
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView, \
    DeleteView
from .models import Lesson, Course
from courses import forms


class CourseListView(ListView):
    model = Course
    paginate_by = 10

    queryset = Course.objects.filter(is_active=True)


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'


class CourseUpdateView(UpdateView):
    model = Course
    success_url = reverse_lazy('courses:index')
    form_class = forms.CourseForm


class CourseCreateView(UpdateView):
    model = Course
    success_url = reverse_lazy('courses:index')
    form_class = forms.CourseForm

class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
def about(request):
    context = {
        'title': 'о нас',
    }
    return render(request, 'courses/about.html', context)
