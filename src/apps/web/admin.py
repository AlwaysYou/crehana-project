from django.contrib import admin
from singlemodeladmin import SingleModelAdmin

# Register your models here.
from .models import InformacionGeneral


@admin.register(InformacionGeneral)
class InformacionGeneralAdmin(SingleModelAdmin):
	pass
