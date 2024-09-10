from django.contrib import admin

from .models import Category, Channel, Country, PlayList, Tag, Subscription, SubEmail, Contact, Forward


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'updated_at', 'created_at')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'updated_at', 'created_at')
    prepopulated_fields = {'slug': ('name',)} 


@admin.register(PlayList)
class PlayListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'updated_at', 'created_at')
    prepopulated_fields = {'slug': ('name',)} 


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'updated_at', 'created_at')
    prepopulated_fields = {'slug': ('name',)} 


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'author', 'link', 'updated_at', 'created_at')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Subscription)
admin.site.register(SubEmail)
admin.site.register(Contact)
admin.site.register(Forward)
