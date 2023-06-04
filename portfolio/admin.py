from django.contrib import admin

from portfolio.models import SiteInfo, Experience, Skill, Awards, Work, Testimonial, MyCV

# Register your models here.
admin.site.register(SiteInfo)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Awards)
admin.site.register(Work)
admin.site.register(Testimonial)
admin.site.register(MyCV)