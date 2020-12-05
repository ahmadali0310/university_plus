from django.shortcuts import render
from .models import Cources, Trainers, Testimonial, Registration, Message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import json


# Create your views here.


def index(request):
    testimonial = Testimonial.objects.all()
    data = {'testimonial': testimonial}
    return render(request, 'index.html', data)


def cources(request):
    cources = Cources.objects.all()
    paginator = Paginator(cources, 5)
    print(paginator.num_pages)
    page = request.GET.get('page')
    print(page)
    cources = paginator.get_page(page)
    testimonial = Testimonial.objects.all()
    data = {'cources': cources, 'testimonial': testimonial}
    return render(request, 'courses.html', data)

def courses_list(request, *args, **kwargs):
    trainer = kwargs.get('trainer')
    if request.is_ajax():
        cources = list(Cources.objects.filter(Trainer__name = trainer).values())
        return JsonResponse({'cources': cources})
    else:
        cources = Cources.objects.all()
        paginator = Paginator(cources, 5)
        print(paginator.num_pages)
        page = request.GET.get('page')
        print(page)
        cources = paginator.get_page(page)
        testimonial = Testimonial.objects.all()
        data = {'cources': cources, 'testimonial': testimonial}
        return render(request, 'courses.html', data)
    


def about(request):
    testimonial = Testimonial.objects.all()
    return render(request, 'about.html', {"testimonial": testimonial})


def contact(request):
    return render(request, 'contact.html')


def trainers(request):
    if request.is_ajax():
        trainer = list(Trainers.objects.all().values())

        return JsonResponse({'trainer': trainer})
    else:
        trainer = Trainers.objects.all()
        paginator = Paginator(trainer, 5)
        print(paginator.num_pages)
        page = request.GET.get('page')
        print(page)
        trainer = paginator.get_page(page)
        testimonial = Testimonial.objects.all()
        return render(request, 'trainers.html', {'trainer': trainer, 'testimonial':testimonial})


def trainer_desc(request, id):
    data = Trainers.objects.get(id=id)
    return render(request, 'trainer_desc.html', {'data': data})


def courseDetail(request, id):
    data = Cources.objects.get(id=id)
    return render(request, 'course_details.html', {'data': data})



def registration(request):
    if request.is_ajax():
        data = json.loads(request.body)

        name = data['name']
        email = data['email']
        number = data['number']
        country = data['counrty']
        trainer = Trainers.objects.get(name=data['teachers'])
        cources = Cources.objects.get(name=data['cources'])
        address = data['address']
        cnic = data['cnic']
        payment = data['payment']
        Registration.objects.create(name= name, email=email, w_number=number, country=country, instructor=trainer, cource=cources, address=address, cnic=cnic, payment_method=payment)
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        subject = "Thank You!!!"
        message = "Thank You for Registration"
        
        send_mail(subject, message,from_email,to_list,fail_silently=True)
        

        return JsonResponse({'created': True})
    else:
         return render(request, 'index.html')


def message(request):
    if request.is_ajax():
        data = json.loads(request.body)
        
        name = data['name']
        email = data['email']
        message = data['message']
        subject = data['subject']

        if len(name) <4 and len(email) <= 10 and len(message) <=5 and len(subject) <=5:
            return JsonResponse({'created': False})
        else:
            Message.objects.create(message=message,  name=name, email=email, subject=subject)

            return JsonResponse({'created': True})
    else:
        return render(request, 'index.html')


