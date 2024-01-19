from django.db import models
# from django.contrib.auth.models import User

from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.


class PythonModel(models.Model):
    title = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='python_post_author', default='Admin')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "PythonModel"
        verbose_name_plural = "PythonModels"

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("PythonModel_detail", kwargs={"pk": self.pk})
