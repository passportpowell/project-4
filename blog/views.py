from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from django.views import generic, View
from .models import Event, Attendee
from .forms import CommentForm, EventForm


class Home(View):
    def get(self, request):
        return render(request, 'index.html')


class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')


class ScheduleView(View):
    def get(self, request):
        return render(request, 'schedule.html')


class PastMeetsView(View):
    def get(self, request):
        return render(request, 'past-meets.html')


class GalleryView(View):
    def get(self, request):
        return render(request, 'gallery.html')


class GameView(View):
    def get(self, request):
        return render(request, 'game.html')


class EventListView(generic.ListView):
    model = Event
    template_name = 'schedule.html'
    context_object_name = 'events'
    queryset = Event.objects.order_by('-date_time')


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'schedule.html'
    context_object_name = 'event'


class PostLike(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class CommentCreateView(View):
    form_class = CommentForm
    template_name = 'comment_create.html'

    def get(self, request, slug):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'slug': slug})

    def post(self, request, slug):
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.event = Event.objects.get(slug=slug)
            comment.save()
            return redirect('event_detail', slug=slug)

        return render(request, self.template_name, {'form': form, 'slug': slug})


@login_required
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('event_detail', slug=event.slug)
    else:
        form = EventForm()
    return render(request, 'blog/event_form.html', {'form': form})
