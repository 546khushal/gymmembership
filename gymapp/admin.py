from django.contrib import admin


# Register your models here.

from .models import NewMemberData

from .models import registerm
from .models import Trainer
from .models import GymImage
from .models import GymImages
from .models import Onsite
from .models import Product
from .models import ProductImage
from .models import supliment
from .models import suplimentImage
from .models import equipment
from .models import equipmentImage
from .models import Blog
from .models import messages,Orderpoduct, Ordersupli, Orderequ
 
admin.site.register(NewMemberData)

admin.site.register(registerm)
admin.site.register(Trainer)
admin.site.register(GymImage)
admin.site.register(GymImages)
admin.site.register(Onsite)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(supliment)
admin.site.register(suplimentImage)
admin.site.register(equipment)
admin.site.register(equipmentImage)
admin.site.register(Blog)
admin.site.register(messages)
admin.site.register(Orderpoduct)
admin.site.register(Ordersupli)
admin.site.register(Orderequ)

