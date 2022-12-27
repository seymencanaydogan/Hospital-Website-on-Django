from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

class Category(MPTTModel):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=400)
    keywords = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by=['title']

    def __str__(self):
        full_path= [self.title]
        k=self.parent
        while k is not None:
            full_path.append(k.title)
            k= k.parent
        return '->'.join(full_path[::-1])

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})
    

class Policlinic(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(blank=True, max_length=300)
    keywords = models.CharField(blank=True, max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    def get_absolute_url(self):
        return reverse("policlinic_detail", kwargs={"slug": self.slug})
    

class Images(models.Model):
    policlinic=models.ForeignKey(Policlinic,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    policlinic=models.ForeignKey(Policlinic,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    comment=models.TextField(max_length=200)
    rate=models.IntegerField(blank=False)
    status = models.CharField(max_length=10, choices=STATUS,default='New')
    ip=models.CharField(max_length=20,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['subject','comment','rate']

class Doctors(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    policlinic=models.ForeignKey(Policlinic,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    linkedin = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

class Randevu(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Onaylandı'),
        ('False', 'Onaylanmadı'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    policlinic=models.CharField(max_length=50)
    doctor=models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    date=models.DateField(null=True)
    time=models.TimeField(null=True)
    payment= models.CharField(max_length=50)
    insurance= models.CharField(max_length=50)
    note=models.TextField(max_length=200)
    status = models.CharField(max_length=15, choices=STATUS,default='New')
    ip=models.CharField(max_length=20,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def str(self):
        return self.user.username

class AppointmentForm(ModelForm):
    class Meta:
        model=Randevu
        fields=['policlinic','doctor','phone','email','date','time','payment','insurance','note']


