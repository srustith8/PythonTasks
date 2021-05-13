from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.conf import settings
# Create your models here.

class UserParent(models.Model):
    user = models.OneToOneField(
        User,on_delete=models.CASCADE,
        primary_key=True,
    )
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporter')

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)

# class Tweet(models.Model):
#     tweet = models.TextField()
#     favourite = models.ManyToManyField('orm_app.User', blank=True, related_name='user_favourite')

#     def __unicode__(self):
#         return self.tweet

# class User(AbstractUser):
#     tweet = models.ManyToManyField(Tweet, blank=True)
#     follower = models.ManyToManyField('orm_app.User', blank=True)
#     pass


#How to add a model for a database view?
class TempUser(models.Model):
    first_name = models.CharField(max_length=100)

    class Meta:
        managed = False 
        db_table = "temp_user"


