from django.contrib import admin
from storage.models import Page, Collection


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass



# Register your models here.
