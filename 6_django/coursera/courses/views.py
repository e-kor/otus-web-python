from django.contrib.auth.decorators import user_passes_test, login_required
from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Lesson, Course


class CourseListView(ListView):
    model = Course
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.all()