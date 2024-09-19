from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Buyer)
admin.site.register(Game)


# admin.site.register(Phones)

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'balance')
    fields = [('name', 'age'), 'balance']
    search_fields = ('name', 'age')
    list_filter = ("name", "age", "balance")


@admin.register(Phones)
class PhonesAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'description', 'year_of_release')
    # fields = [('name', 'age'), 'balance']
    search_fields = ('title', 'year_of_release')
    list_filter = ("title", "cost", "year_of_release")
    # разделение по секциям NB!fieldsets must be a list or tuple
    fieldsets = (
        ('info', {
            'fields':
                ('title', 'cost', 'year_of_release')
        }),
        ('footer', {
            'fields':
                ('id','description')
        })
    )
