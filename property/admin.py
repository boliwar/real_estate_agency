from django.contrib import admin

from .models import Flat, Complaint, Owner

class FlatInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner', 'flat')


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ["created_at",]
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town' )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'active', 'has_balcony', 'town', )
    raw_id_fields = ('liked_users', )
    inlines = [FlatInline]

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user','flat')

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flats',)
    search_fields = ('owner',)
    inlines = [FlatInline]

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)

