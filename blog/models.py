from django.db import models

# Create your models here.
#Every class is a table and every var in that class are the column of that class

class Post(models.Model):
	title=models.CharField(max_length = 140)  # CharField is use for Short text
	body=models.TextField()    #TextField is use for long text
	date=models.DateTimeField()  #for date and time
	
	def __str__(self):
		return self.title   #For reference or list  the title furter we need it