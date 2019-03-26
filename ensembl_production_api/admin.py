# -*- coding: utf-8 -*-
from django.contrib import admin

from ensembl_production.admin import ProductionUserAdminMixin
from .models import *


class ProductionModelAdmin(ProductionUserAdminMixin):
    list_per_page = 50
    readonly_fields = ('created_by', 'created_at', 'modified_by', 'modified_at')


class ProductionTabularInline(admin.TabularInline):
    readonly_fields = ('modified_by', 'created_by', 'created_at', 'modified_at')


class AttribInline(ProductionTabularInline):
    model = MasterAttrib
    extra = 1
    fields = ['value', 'modified_by', 'created_by', 'created_at', 'modified_at']


class AttribSetInline(ProductionTabularInline):
    model = MasterAttribSet
    extra = 1
    fields = ['attrib_set_id', 'modified_by', 'created_by', 'created_at', 'modified_at']


class AnalysisDescriptionInline(ProductionTabularInline):
    model = AnalysisDescription
    extra = 1
    fields = ['logic_name', 'display_label', 'description', 'web_data', 'db_version', 'displayable']


# Register your models here.
class AttribTypeAdmin(ProductionModelAdmin):
    list_display = ('code', 'name', 'description')
    search_fields = ('code', 'name', 'description')
    inlines = (AttribInline,)


class AttribAdmin(ProductionModelAdmin):
    list_display = ('value', 'attrib_type')
    search_fields = ('value', 'attrib_type__name')
    inlines = (AttribSetInline,)


class AttribSetAdmin(ProductionModelAdmin):
    fields = ('attrib_set_id', 'attrib', 'is_current', ('created_by', 'modified_by'))
    list_display = ('attrib', 'attrib_set_id')
    search_fields = ('attrib__value', 'attrib_set_id')


class BioTypeAdmin(ProductionModelAdmin):
    # TODO DBTYPE to add display inline+flex class
    fields = ('name', 'object_type', 'db_type', 'biotype_group', 'attrib_type', ('is_dumped', 'is_current'),
              'description', ('created_by', 'modified_by'))
    list_display = ('name', 'object_type', 'db_type', 'biotype_group', 'attrib_type', 'is_dumped', 'description')
    search_fields = ('name', 'object_type', 'db_type', 'biotype_group', 'attrib_type__name', 'description')


class AnalysisDescriptionAdmin(ProductionModelAdmin):
    fields = ('logic_name', 'description', 'display_label', ('db_version', 'displayable', 'is_current',),
              ('created_by', 'modified_by'))

    list_display = ('logic_name', 'display_label', 'description', 'web_data', 'db_version', 'displayable')
    search_fields = ('logic_name', 'display_label', 'description', 'web_data__data')


class MetakeyAdmin(ProductionModelAdmin):
    list_display = ('name', 'is_optional', 'db_type', 'description')
    search_fields = ('name', 'db_type', 'description')


class WebDataAdmin(ProductionModelAdmin):
    list_display = ('data', 'comment')
    search_fields = ('data', 'comment')
    inlines = (AnalysisDescriptionInline,)


class MasterExternalDbAdmin(ProductionModelAdmin):
    list_display = (
        'db_name', 'db_release', 'status', 'db_display_name', 'priority', 'type', 'secondary_db_name',
        'secondary_db_table')
    search_fields = (
        'db_name', 'db_release', 'status', 'db_display_name', 'priority', 'type', 'secondary_db_name',
        'secondary_db_table')


admin.site.register(AnalysisDescription, AnalysisDescriptionAdmin)
admin.site.register(MasterAttribType, AttribTypeAdmin)
admin.site.register(MasterAttrib, AttribAdmin)
admin.site.register(MasterAttribSet, AttribSetAdmin)
admin.site.register(MasterBiotype, BioTypeAdmin)
admin.site.register(MetaKey, MetakeyAdmin)
admin.site.register(WebData, WebDataAdmin)
admin.site.register(MasterExternalDb, MasterExternalDbAdmin)
