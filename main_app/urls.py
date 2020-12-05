from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="main"),
    path('courses/', views.cources, name="cources"),
    path('courses_list/<str:trainer>/', views.courses_list, name="courses_list"),
    path('trainers/', views.trainers, name="trainers"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('message/', views.message, name="message"),
    path('registration/', views.registration, name="registration"),
    path('trainer_desc/<int:id>', views.trainer_desc, name="trainer_desc"),
    path('courseDetail/<int:id>', views.courseDetail, name="courseDetail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
