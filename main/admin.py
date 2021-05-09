from django.contrib import admin
from .models import News
from .models import TeachersDetail
from .models import Teacher
from .models import Students
from .models import Contacts
from .models import Feed

admin.site.register(News)
admin.site.register(TeachersDetail)
admin.site.register(Teacher)
admin.site.register(Students)
admin.site.register(Contacts)
admin.site.register(Feed)