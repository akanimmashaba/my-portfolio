from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin, HitCount


# Create your models here.




class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class MetaData(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        abstract = True
        

class Tag(MetaData,Timestamp):
    def __str__(self):
        return self.title
            
            
class Category(MetaData,Timestamp):
    def __str__(self):
        return self.title
    
class Post(HitCountMixin,MetaData,Timestamp):
    STATUS_CHOICES = (
        ('drafted', 'Drafted'),
        ('published', 'Published'),
    )

    description = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='drafted')
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    