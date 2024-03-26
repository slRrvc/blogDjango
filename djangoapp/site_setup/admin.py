from django.contrib import admin
from django.http.request import HttpRequest
from site_setup.models import MenuLink, SiteSetup


# @admin.register(MenuLink)
# class MenuLinkAdmin(admin.ModelAdmin):
#     list_display = 'text', 'url_or_path',
#     list_display_links = 'text', 'url_or_path',
#     search_fields = 'text', 'url_or_path',


class MenuLinkInLine(admin.StackedInline):
    model = MenuLink
    extra = 0


@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = 'title', 'description',
    inlines = MenuLinkInLine,

    def has_add_permission(self, request: HttpRequest) -> bool:
        return not SiteSetup.objects.exists()