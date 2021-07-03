from django.contrib import admin
from .models import News
from .models import Teacher
from .models import Students
from .models import Contacts
from .models import Feed
from .models import Achievements
from .models import Nomenklatura

admin.site.register(News)
admin.site.register(Teacher)
admin.site.register(Students)
admin.site.register(Contacts)
admin.site.register(Feed)
admin.site.register(Achievements)
admin.site.register(Nomenklatura)