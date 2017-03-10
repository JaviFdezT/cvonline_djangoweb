from django.contrib import admin
from .models import PersonalData,Projects,WorkExperience,Conferences,Education,Languages,DigComps,Router,ImgProfile
from django.contrib.sites.models import Site
from django import forms
from itertools import chain
import os
import time

admin.site.unregister(Site)

class ConfAdmin(admin.ModelAdmin):  
    list_display = ('title', 'dates','owner')
    def get_queryset(self, request):
          qs = super(ConfAdmin, self).get_queryset(request)
          if request.user.is_superuser:
              return qs
          return qs.filter(owner=request.user.username)
    def add_view(self, *args, **kwargs):
        self.fields = ('title','dates','organization','description')
        return super(ConfAdmin, self).add_view(*args, **kwargs)
    def change_view(self, *args, **kwargs):
        self.fields = ('title','dates','organization','description')
        return super(ConfAdmin, self).change_view(*args, **kwargs) 
    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        obj.save()

class CompAdmin(admin.ModelAdmin): 
    list_display = ('comp', 'owner')
    def get_queryset(self, request):
          qs = super(CompAdmin, self).get_queryset(request)
          if request.user.is_superuser:
              return qs
          return qs.filter(owner=request.user.username)

    def add_view(self, *args, **kwargs):
        self.fields = ('comp','infoprocessing','contentcreation','safety','problemsolving')
        return super(CompAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.fields = ('comp','infoprocessing','contentcreation','safety','problemsolving')
        return super(CompAdmin, self).change_view(*args, **kwargs) 

    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        obj.save()
    
class LangAdmin(admin.ModelAdmin): 
    list_display = ('language', 'owner')
    def get_queryset(self, request):
          qs = super(LangAdmin, self).get_queryset(request)
          if request.user.is_superuser:
              return qs
          return qs.filter(owner=request.user.username)
    def add_view(self, *args, **kwargs):
        self.fields = ('language','written','spoken','understood','native')
        return super(LangAdmin, self).add_view(*args, **kwargs)
    def change_view(self, *args, **kwargs):
        self.fields = ('language','written','spoken','understood','native')
        return super(LangAdmin, self).change_view(*args, **kwargs) 
    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        obj.save()
  
class ProjAdmin(admin.ModelAdmin): 
    list_display = ('name', 'owner')
    def get_queryset(self, request):
          qs = super(ProjAdmin, self).get_queryset(request)
          if request.user.is_superuser:
              return qs
          return qs.filter(owner=request.user.username)
    def add_view(self, *args, **kwargs):
        self.fields = ('name','language','filename','url')
        return super(ProjAdmin, self).add_view(*args, **kwargs)
    def change_view(self, *args, **kwargs):
        self.fields = ('name','language','filename','url')
        return super(ProjAdmin, self).change_view(*args, **kwargs) 
    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        obj.save()
    
class WorkAdmin(admin.ModelAdmin): 
    list_display = ('position','dates','owner')
    def get_queryset(self, request):
          qs = super(WorkAdmin, self).get_queryset(request)
          if request.user.is_superuser:
              return qs
          return qs.filter(owner=request.user.username)
    def add_view(self, *args, **kwargs):
        self.fields = ('position','dates','organization','description')
        return super(WorkAdmin, self).add_view(*args, **kwargs)
    def change_view(self, *args, **kwargs):
        self.fields = ('position','dates','organization','description')
        return super(WorkAdmin, self).change_view(*args, **kwargs) 
    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        obj.save()
   
class EduAdmin(admin.ModelAdmin): 
    list_display = ('title','dates','owner')
    def get_queryset(self, request):
          qs = super(EduAdmin, self).get_queryset(request)
          if request.user.is_superuser:
              return qs
          return qs.filter(owner=request.user.username)
    def add_view(self, *args, **kwargs):
        self.fields = ('title','dates','organization','description','certificate')
        return super(EduAdmin, self).add_view(*args, **kwargs)
    def change_view(self, *args, **kwargs):
        self.fields = ('title','dates','organization','description','certificate')
        return super(EduAdmin, self).change_view(*args, **kwargs) 
    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        obj.save()
    
class PDataAdmin(admin.ModelAdmin): 
    list_display = ('name','initials')
    def get_queryset(self, request):
          qs = super(PDataAdmin, self).get_queryset(request)
          if request.user.is_superuser:
              return qs
          return qs.filter(initials=request.user.username)
    def add_view(self, *args, **kwargs):
        self.fields = ('initials','email')
        return super(PDataAdmin, self).add_view(*args, **kwargs)
    def change_view(self, *args, **kwargs):
        self.fields = ('name','address','city','code','country','phonenumber','mail','datebirth','nationality','profile','linkedin','github')
        return super(PDataAdmin, self).change_view(*args, **kwargs) 
    def save_model(self, request, obj, form, change):
        if not obj.initials:
            obj.initials = request.user
        obj.save()

class RouterAdmin(admin.ModelAdmin): 
    list_display = ('specifications','date','owner')
    def get_queryset(self, request):
          qs = super(RouterAdmin, self).get_queryset(request)
          if request.user.is_superuser:
              return qs
          return qs.filter(owner=request.user.username)
    def add_view(self, *args, **kwargs):
        self.fields = ('specifications',)
        return super(RouterAdmin, self).add_view(*args, **kwargs)
    def change_view(self, *args, **kwargs):
        self.fields = ('specifications',)
        return super(RouterAdmin, self).add_view(*args, **kwargs)
    def save_model(self, request, obj, form, change):
        objects=Router.objects.filter(owner=request.user)
        if objects.count() == 1:
            objects[0].delete()
        if not obj.owner:
            obj.owner = request.user
        obj.save()

class ImgAdmin(admin.ModelAdmin): 
    list_display = ('specifications','date','owner')
    def get_queryset(self, request):
          qs = super(ImgAdmin, self).get_queryset(request)
          if request.user.is_superuser:
              return qs
          return qs.filter(owner=request.user.username)
    def add_view(self, *args, **kwargs):
        self.fields = ('specifications',)
        return super(ImgAdmin, self).add_view(*args, **kwargs)
    def change_view(self, *args, **kwargs):
        self.fields = ('specifications',)
        return super(ImgAdmin, self).add_view(*args, **kwargs)
    def save_model(self, request, obj, form, change):
        if not obj.owner:
            obj.owner = request.user
        if ImgProfile.objects.filter(owner=request.user).count() == 1:
            ImgProfile.objects.filter(owner=request.user)[0].delete()
        obj.save()


admin.site.register(Router,RouterAdmin)
admin.site.register(ImgProfile,ImgAdmin)
    
admin.site.register(PersonalData,PDataAdmin)
admin.site.register(Projects,ProjAdmin)
admin.site.register(WorkExperience,WorkAdmin)
admin.site.register(Conferences,ConfAdmin)
admin.site.register(Education,EduAdmin)
admin.site.register(Languages,LangAdmin)
admin.site.register(DigComps,CompAdmin)

