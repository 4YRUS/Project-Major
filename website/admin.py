from django.contrib import admin
from .models import Customer,Product,Order,Tag,Images,Topic,SubTopic,PDFs

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)
admin.site.register(Images)
admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(PDFs)

# Register your models here.
