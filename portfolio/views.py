from django.shortcuts import render
from django.views.generic import TemplateView

from portfolio.models import SiteInfo, Experience, Skill, Awards, Work, Testimonial, MyCV


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['site_information'] = SiteInfo.objects.first()
        context ['experiences'] = Experience.objects.all()
        context ['skills'] = Skill.objects.all()
        context ['award'] = Awards.objects.all()
        context ['works'] = Work.objects.all()
        context ['testimonials'] = Testimonial.objects.all()
        context['mycv'] = MyCV.objects.last()
        return context
