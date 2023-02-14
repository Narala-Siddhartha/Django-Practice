"""TestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TestProject import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name='home page'),
    path('about/',views.aboutUS,name='aboutus'),
    path('course/',views.course,name='course'),
    path('course/<int:courseid>',views.courseDetail,name='courseDetail'),
    path('userform/',views.userForm,name="userForm"),
    path('secureuserform/',views.secureUserForm,name="secureuserform"),
    path('success/',views.success,name='success'),
    path('calculator/',views.Calculator,name="calculator"),
    path('evenodd/',views.EvenOdd,name="evenodd"),
    path('persondetails/<personid>',views.PersonDetail,name="PersonDetail"),
    path('savedata/',views.SaveData,name="savedata"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
