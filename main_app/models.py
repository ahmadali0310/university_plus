from django.db import models

# Create your models here.


class Trainers(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='profile_pics')
    description = models.CharField(max_length=10000)
    l_description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Cources(models.Model):
    Trainer = models.ForeignKey(Trainers, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=10000)
    l_description = models.CharField(max_length=1000)
    pay = models.IntegerField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=300)
    feedBack = models.CharField(max_length=10000)
    pic = models.ImageField(upload_to='testimonials')


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    w_number = models.IntegerField();
    country = models.CharField(max_length=100)
    instructor = models.ForeignKey(Trainers, on_delete=models.CASCADE);
    cource = models.ForeignKey(Cources, on_delete=models.CASCADE);
    address = models.CharField(max_length=254)
    cnic = models.IntegerField()
    payment_method = models.CharField(max_length=30);


    def __str__(self):
        return self.name


class Message(models.Model):
    message = models.CharField(max_length=2000)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.name