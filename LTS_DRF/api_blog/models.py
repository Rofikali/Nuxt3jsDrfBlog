from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# from django.urls import reverse
# from django.conf import settings

# User = settings.AUTH_USER_MODEL


class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author')
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title

        # return self.title

        # for i in self.title:
        #     print(i)
        #     break

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk': self.pk})
