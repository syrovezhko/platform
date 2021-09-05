from django.shortcuts import render
from.models import Enrollment
from cms.models import CmsSections
from cms.models import TeachersCard
#from teachers.models import TeachersCard

# Create your views here.


def first_page(request):
    section_list = CmsSections.objects.all()
    teachers_list = TeachersCard.objects.all()
    return render(request, './index.html', {'section_list': section_list,
                                            'teachers_list': teachers_list})
    #object_list = Enrollment.objects.all()
   # return render(request, './index.html', {'object_list': object_list})

def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        kname = request.POST['kname']
        number = request.POST['number']
        phone = request.POST['phone']
        section = request.POST['section']
        element = Enrollment(enrollment_name=name, enrollment_kname=kname ,enrollment_age=number, enrollment_phone=phone, enrollment_section=section)
        element.save()
        return render(request, './thanks.html', {'name': name,
                                                 'section': section})
    else:
        return render(request, './thanks.html')



