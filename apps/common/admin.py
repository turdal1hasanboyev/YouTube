from django.contrib import admin

from .models import Category, Channel, Country, PlayList, Tag, Subscription, SubEmail


admin.site.register(Category)
admin.site.register(Channel)
admin.site.register(Country)
admin.site.register(PlayList)
admin.site.register(Tag)
admin.site.register(Subscription)
admin.site.register(SubEmail)
