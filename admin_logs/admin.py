from django.contrib import admin
from django.template import loader

from admin_logs.models import Request


class RequestAdmin(admin.ModelAdmin):
    class Meta:
        app_label = 'Admin logs'

    class Media(object):
        css = {
            'all': ('css/admin_logs/styles.css',)
        }
        js = (
            'js/admin_logs/common.js',
        )

    list_display = ('id', 'short_message')

    list_filter = ('status_code', 'max_level')

    search_fields = ('ip', 'status_code')

    def short_message(self, obj):
        data = {
            'admin_log': obj,
        }
        return loader.render_to_string("admin_logs/admin_logs_list.html", data)
    short_message.allow_tags = True

    def has_add_permission(self, request):
        return False


admin.site.register(Request, RequestAdmin)
