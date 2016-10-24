from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from apis.mail import send_mail


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# 댓글을 저장하는 데이터베이스 모델
class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        print(self.post.author.email)
        recipient_list = [self.post.author.email]
        send_mail('댓글이 달렸습니다', '확인해보세요')