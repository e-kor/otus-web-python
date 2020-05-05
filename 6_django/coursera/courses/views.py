from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, FormView, ListView, \
    TemplateView, UpdateView
from rest_framework.viewsets import ModelViewSet

from courses import forms
from courses.serializers import CourseListSerializer, CourseSerializer
from .models import Course


class CourseListView(ListView):
    model = Course
    paginate_by = 10

    queryset = Course.objects.filter(is_active=True)


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'


class CourseUpdateView(UpdateView):
    model = Course
    form_class = forms.CourseForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['lessons'] = forms.LessonFormSet(self.request.POST,
                                                  instance=self.object)
        else:
            data['lessons'] = forms.LessonFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        lessons_data = context['lessons']
        with transaction.atomic():
            self.object = form.save()
            if lessons_data.is_valid():
                lessons_data.instance = self.object
                lessons_data.save()
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return f'/course/detail/{self.object.pk}/'


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


class ContactView(FormView):
    template_name = 'courses/contact.html'
    form_class = forms.ContactForm
    success_url = reverse_lazy('courses:thankyou')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'courses/thankyou.html'


class CourseAPIViewSet(ModelViewSet):
    model = Course
    queryset = (Course.objects.all()
                .select_related('tutor', )
                .prefetch_related('lessons', 'lessons__tags', 'tags', ))

    # serializer_class = CourseSerializer
    # permission_classes = (IsAuthenticated,)
    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        return CourseSerializer
