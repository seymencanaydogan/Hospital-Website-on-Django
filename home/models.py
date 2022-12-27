from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from django.forms import ModelForm, TextInput, Textarea

class Setting(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(max_length=50)
    smptpserver = models.CharField(blank=True, max_length=30)
    smptemail = models.CharField(blank=True, max_length=30)
    smptpassword = models.CharField(blank=True, max_length=150)
    smptport = models.CharField(blank=True, max_length=15)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    contact_map = models.CharField(max_length=500)
    weekdays=models.CharField(blank=True, max_length=30)
    saturday=models.CharField(blank=True, max_length=30)
    sunday=models.CharField(blank=True, max_length=30)
    references = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    uptade_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactFormMessage(models.Model):
    STATUS= (
        ('New','New'),
        ('Read','Read'),
        ('Closed','Closed'),
    )
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=255)
    status=models.CharField(blank=True, max_length=10, choices=STATUS, default='New')
    ip=models.CharField(blank=True, max_length=20)
    note=models.CharField(blank=True, max_length=100)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ContactFormu(ModelForm):
    class Meta:
        model=ContactFormMessage
        fields=['name','email','subject','message']
        widgets= {
            'name': TextInput(attrs={'class':'input','placeholder':'Ad & Soyad'}),
            'subject': TextInput(attrs={'class':'input','placeholder':'Konu'}),
            'email': TextInput(attrs={'class':'input','placeholder':'E-Mail'}),
            'message': TextInput(attrs={'class':'input','placeholder':'Mesajınız','rows':'5'}),
        }

class UserProfile(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    adress = models.CharField(blank=True,max_length=150)
    city = models.CharField(blank=True,max_length=30)
    country = models.CharField(blank=True,max_length=30)
    status=models.CharField(blank=True, max_length=10, choices=STATUS)
    image=models.ImageField(blank=True,upload_to='images/users/')
    def str(self):
        return self.user.username

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

class FAQ(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    question=models.CharField(max_length=200)
    answer=models.TextField()
    status=models.CharField(blank=True, max_length=10, choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question