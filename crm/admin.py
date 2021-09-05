from django.contrib import admin
from .models import Enrollment, StatusCrm, CommentCrm

# Register your models here.
class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 0

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'enrollment_dt',
                    'enrollment_status',
                    'enrollment_name',
                    'enrollment_kname',
                    'enrollment_age',
                    'enrollment_section',
                    'enrollment_phone')
    list_display_links = ('id', 'enrollment_name')
    search_fields = ('id', 'enrollment_dt',
                     'enrollment_name',
                     'enrollment_kname',
                     'enrollment_phone')
    list_filter = ('enrollment_status',
                   'enrollment_age',
                   'enrollment_section',)
    list_editable = ('enrollment_status', 'enrollment_phone')
    list_per_page = 10
    list_max_show_all = 100
    fields = ('id', 'enrollment_dt',
              'enrollment_status',
              'enrollment_name',
              'enrollment_phone',
              'enrollment_kname',
              'enrollment_age',
              'enrollment_section')
    readonly_fields = ('id', 'enrollment_dt')
    #поле класса коммент
    inlines = [Comment,]

admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
