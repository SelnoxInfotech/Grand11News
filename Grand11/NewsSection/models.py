from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):               #category table
    name=models.CharField(max_length=500)
    # Status=models.CharField(max_length=20,default=1,choices=Status)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
    
   
    
class SubCategory(models.Model):            #Subcategory table
    name=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    # Status=models.CharField(max_length=20,default=1,choices=Status)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class News(models.Model):                       #News
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    SubCategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,blank=True,default=None,null=True)
    Title=models.CharField(max_length=100,default=None)
    Description=RichTextField()
    Image=models.ImageField(upload_to='media/News',default=None)
    Alt_Text=models.CharField(max_length=50,default=None,blank=False)
    Link=models.URLField(max_length=200,blank=True,default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.Title


class VideoNews(models.Model):                       #News
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    SubCategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,blank=True,default=None,null=True)
    Title=models.CharField(max_length=100,default=None)
    Description=RichTextField()
    Video=models.FileField(upload_to='media/News',default=None)
    VideoUrl=models.URLField(max_length=200,blank=True,default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.Title

