from django.db import models
from django.contrib.auth.models import User

class QnA(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='QnA/',blank=True, null=True)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to="Reviews/",blank=True, null=True)

    def __str__(self):
        return self.title