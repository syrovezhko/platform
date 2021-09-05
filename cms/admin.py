from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import CmsSections, TeachersCard
#from .models import TeachersCard

# Register your models here.
class CmsSectionsAdmin(admin.ModelAdmin):
    model = CmsSections
    list_display = ('cms_titleCard',
                    'cms_age',
                    'cms_termMonths',
                    'cms_regularity',
                    'cms_level')
    list_display_links = ('cms_titleCard',
                          'cms_age',
                          'cms_termMonths',
                          'cms_regularity',
                          'cms_level')

class TeachersCardAdmin(admin.ModelAdmin):
    model = TeachersCard
    list_display = ('teachersCard_lname', 'teachersCard_name', 'teachersCard_phone', 'get_img')
    list_display_links = ('teachersCard_lname', 'teachersCard_name', 'get_img')
    fields = ('teachersCard_dt',
              'get_img',
              'teachersCard_img',
              'teachersCard_name',
              'teachersCard_lname',
              'teachersCard_phone',
              'teachersCard_tg',
              'teachersCard_email',
              'teachersCard_degree1',
              'teachersCard_degreeYear1',
              'teachersCard_teacherDegree1',
              'teachersCard_teacherDegreeYear1',
              'teachersCard_teacherDegree2',
              'teachersCard_teacherDegreeYear2',
              'teachersCard_teacherDegree3',
              'teachersCard_teacherDegreeYear3',
              'teachersCard_subject1',
              'teachersCard_subject2',
              'teachersCard_subject3',
              'teachersCard_subject4',
              'teachersCard_subject5',
              'teachersCard_subject6',
              'teachersCard_subject7',
              'teachersCard_subject8',
              'teachersCard_subject9',
              'teachersCard_subject10',
              'teachersCard_subject11')
    readonly_fields = ('get_img', 'teachersCard_dt',)

    def get_img(self, obj):
        if obj.teachersCard_img:
            return mark_safe(f'<img src="{obj.teachersCard_img.url}" width="80px">')
        else:
            return 'нет картинки'

    get_img.short_description = 'Миниатюра'


admin.site.register(CmsSections, CmsSectionsAdmin)
admin.site.register(TeachersCard, TeachersCardAdmin)