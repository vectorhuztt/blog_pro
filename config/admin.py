from django.contrib import admin

from config.models import Link, SideBar
from typeidea.base_admin import BaseOwnerAdmin


@admin.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'owner', 'created_at')
    fields = ('title', 'href', 'status', 'weight')


@admin.register(SideBar)
class SidebarAdmin(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_at')
    fields = ('title', 'display_type', 'content')
