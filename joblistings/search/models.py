from django.db import models

# Create your models here.
class JobLink(models.Model):
	text = models.TextField(default='')
	post_id = models.AutoField(primary_key=True)
	summary = models.TextField(default='')
