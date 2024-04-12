from django.contrib import admin


# Register your models here.

from .models import NewMemberData
from .models import Product
from .models import registerm
from .models import Trainer


admin.site.register(NewMemberData)
admin.site.register(Product)
admin.site.register(registerm)
admin.site.register(Trainer)