from django.contrib import admin

from .models import Flat, Complaint

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner')
    readonly_fields = ["created_at",]
    list_display = ('address', 'owner_pure_phone', 'price', 'new_building', 'construction_year', 'town' )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'active', 'has_balcony', 'town', )
    raw_id_fields = ('liked_users',)

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('complaint_user','complaint_flat')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

