"""Admin MVC"""
from django.contrib import admin
from django.utils.html import format_html_join
from api.models import CnabTemplate, ImportTemplate, \
    ImportCnabTemplate, TransactionTypeTemplate


class ImportCnabTemplateInline(admin.TabularInline):
    """ImportCnabTemplate Inline"""
    model = ImportCnabTemplate
    extra = 1


class ImportTemplateAdmin(admin.ModelAdmin):
    """ImportCnabTemplate Admin"""
    inlines = (ImportCnabTemplateInline,)
    list_display = ['description', 'get_templates']

    def get_templates(self, obj):
        """Get templates"""
        return format_html_join(
            '\n', "<li>{} - {}</li>",
            ((o.description,o.commentary) for o in obj.template.all())
        )

    get_templates.short_description = "Campos CNAB"


class CnabTemplateAdmin(admin.ModelAdmin):
    """CnabTemplate Admin"""
    list_display = ['description', 'start', 'end', 'size', 'commentary']


class TransactionTypeTemplateAdmin(admin.ModelAdmin):
    """TransactionTypeTemplate Admin"""
    list_display = ['description', 'operation', 'signal']


admin.site.register(TransactionTypeTemplate, TransactionTypeTemplateAdmin)
admin.site.register(CnabTemplate, CnabTemplateAdmin)
admin.site.register(ImportTemplate, ImportTemplateAdmin)
