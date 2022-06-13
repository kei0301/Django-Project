from django.contrib import admin
from .models import Domain, Csv, Images, Template, configTemplate
from django.contrib import messages


class domainAdmin(admin.ModelAdmin):
    list_display = ('cname', 'status')
    search_fields = ('host_name + Cna',)


class csvAdmin(admin.ModelAdmin):
    list_display = ('csvName', 'csvUrl')
    search_fields = ('csvName', 'csvUrl')


class folderAdmin(admin.ModelAdmin):
    list_display = ('folder', 'imgLinks')
    search_fields = ('folder',)


class templateAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'file', 'folder')
    search_fields = ('name', 'domain', 'file', 'folder')


class configAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Domain, domainAdmin)
admin.site.register(Csv, csvAdmin)
admin.site.register(Images, folderAdmin)
admin.site.register(Template, templateAdmin)
admin.site.register(configTemplate, configAdmin)
