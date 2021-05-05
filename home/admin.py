from django.contrib import admin
from home.models import profileinfo,contact_us, Message


admin.site.site_header="JeevanBandhan"

class profileinfoAdmin(admin.ModelAdmin):
    list_display = ['user','pk','pro_Id','city','gender','dob','conttact_no','date_joined']
    search_fields = ['pro_Id','gender']
    list_filter = ['pro_Id','gender']
    list_editable = ['conttact_no','dob']

class contact_usAdmin(admin.ModelAdmin):
    list_display = ['name','email','mo_no','msg']
    search_fields = ['name','email','mo_no','msg']

admin.site.register(profileinfo,profileinfoAdmin)
admin.site.register(contact_us,contact_usAdmin)
admin.site.register(Message)
