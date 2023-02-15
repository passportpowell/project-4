from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
likes = models.ManyToManyField(User, related_name='liked_posts')


class MyModel(models.Model):
    my_field = RichTextField()


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    image = CloudinaryField('image', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.TextField()
    date_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"
