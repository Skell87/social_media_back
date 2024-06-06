from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
      return self.user.username
    
class UserPost(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   content = models.TextField()
   date_created = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return f'user: {self.user}, content: {self.content}, created: {self.date_created}'