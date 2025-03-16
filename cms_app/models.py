from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from PIL import Image
from django.shortcuts import render, get_object_or_404

# Create your models here.

class Topic(models.Model):
    '''A topic that user will add the content about.'''
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        '''Return a string representation of the instance of the model.'''
        return self.title
    
    
    def get_absolute_url(self):
       return reverse('create-entry')
    

class Entries(models.Model):
    '''Entries and Topic will have many to one relationship'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    entries_image = models.ImageField(default= 'default.jpg', upload_to ='images')
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

   
    def __str__(self):
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        else:
            return f'{self.text[:50]}'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.entries_image.path)
        if img.height > 500 and img.width > 500:
            output_size = (500,500) 
            img.thumbnail(output_size)
            img.save(self.entries_image.path)
        
    def get_absolute_url(self):
        return reverse('all-content', kwargs = {'pk':self.topic.id})
    
    @property
    def number_of_comments(self):
        return Comment.objects.filter(entries=self).count()

    
class Comment(models.Model):
    
    entries = models.ForeignKey(Entries, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ', ' + self.entries.name[:40]


    

    

        


   



