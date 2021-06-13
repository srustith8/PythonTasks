from django.contrib import admin
from .models import Rule,Channel
from .models import Officer, Rank, Ship

# Register your models here.
class ChannelAdmin(admin.TabularInline):
    model = Channel

class RuleAdmin(admin.ModelAdmin):
    model = Rule
    inlines = [ChannelAdmin,]

# class OfficerTabularInline(admin.TabularInline):
#     model = Officer


class OfficerAdmin(admin.ModelAdmin):
    model = Officer
    list_display = ['name', 'rank']


# class ShipAdmin(admin.ModelAdmin):
#     inlines = [OfficerTabularInline]
#     model = Ship
#     list_display = ['name', 'registry']


class RankAdmin(admin.ModelAdmin):
    model = Rank
    list_display = ['name']


class OfficerStackedInline(admin.StackedInline):
    model = Officer

class ShipAdmin(admin.ModelAdmin):
    inlines = [OfficerStackedInline]
    model = Ship
    list_display = ['name', 'registry']

# Register your models here.
admin.site.register(Officer, OfficerAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Ship, ShipAdmin)

admin.site.register(Rule,RuleAdmin)
