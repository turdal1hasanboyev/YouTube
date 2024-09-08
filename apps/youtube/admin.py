from django.contrib import admin

from .models import Content, Liked, Comment, SavedForLater, Premiera


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'link',
        'category',
        'channel',
        'country',
        'play_list',
        'like',
        'dislike',
        'forward',
        'premiere_date',
        'language',
        'updated_at',
        'created_at',
        )

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Liked)
admin.site.register(Comment)
admin.site.register(SavedForLater)
admin.site.register(Premiera)
