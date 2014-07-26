from django.db import models
# #Create your models here.

class JobPost(models.Model):
	title = models.CharField(max_length=50)
	posted = models.CharField(max_length=15) # Date?
	#keywords = ListField() # ???
	original_post_link = models.CharField(max_length=50)
	location = models.CharField(max_length=50)
	job_title = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	map_link = models.CharField(max_length=50)
	compensation = models.CharField(max_length=50)
	#skills = ListField()
	#experience = ListField()
	# tokenized_text = ListField() # don't store tokenized text
	text = models.CharField(max_length=500)
	_id = models.AutoField(primary_key=True)

class Keyword(models.Model):
	word = models.CharField(max_length=50)
	_id = models.AutoField(primary_key=True)

class Skill(models.Model):
	skill = models.CharField(max_length=50)
	_id = models.AutoField(primary_key=True)

class Experience(models.Model):
	experience = models.TextField()
	_id = models.AutoField(primary_key=True)

class JobKeyword(models.Model):
	word_id = models.IntegerField()
	post_id = models.IntegerField()

class JobSkill(models.Model):
	skill_id = models.IntegerField()
	post_id = models.IntegerField()

class JobExperience(models.Model):
	experience_id = models.IntegerField()
	post_id = models.IntegerField()

# add user class and relationships

# class JobLink(models.Model):
# 	text = models.CharField(max_length=50)
# 	post_id = models.CharField(primary_key=True, max_length=50)
# 	summary = models.CharField(max_length=150)

# class JobLink(Document):
# 	title = StringField(max_length=50)
# 	post_id = IntField()
# 	summary = StringField(max_length=200)

# class JobPost(Document):
# 	title = StringField(max_length=100)
# 	posted = DateTimeField(help_text='date posted')
# 	keywords = ListField(StringField(max_length=50))
# 	original_post_link = StringField(max_length=100)
# 	location = StringField(max_length=100)
# 	job_title = StringField(max_length=100)
# 	address = StringField(max_length=150)
# 	map_link = StringField(max_length=150)
# 	compensation = StringField(max_length=100)
# 	skills = ListField(StringField(max_length=100))
# 	experience = ListField(StringField(max_length=100))
# 	text = StringField(max_length=2500)