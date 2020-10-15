from django.db import models
from django.utils import timezone
from django.urls import reverse

#Post model
class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    text = models.CharField(max_length=2000000)
    title = models.CharField(max_length=500)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})


#Comment Model
class Comment(models.Model):
    Post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.CharField(blank=False,max_length=500)
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def approve(self):
        self.approved_comment = True
        self.save()

    def absolute_url(self):
        return reverse('post_list')
