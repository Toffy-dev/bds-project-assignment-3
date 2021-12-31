from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from main.models import Customer



class CustomerAdmin(UserAdmin):
	list_display = ('id','email','username','date_joined', 'last_login', 'is_admin','is_staff', 'phone_number', 'balance')
	search_fields = ('id','email','username',)
	readonly_fields=('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Customer, CustomerAdmin)