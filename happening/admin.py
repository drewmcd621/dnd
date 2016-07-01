from django.contrib import admin

# Register your models here.
from happening.models import Game



class GameAdmin(admin.ModelAdmin):

    def queryset(self, request):
            qs = super(GameAdmin, self).queryset(request)

            if request.user.is_superuser:
                return qs

            #Only show their own game model to them
            return qs.filter(host=request.user)

    def save_model(self, request, obj, form, change):
        obj.host = request.user
        obj.save()

admin.site.register(Game, GameAdmin)
