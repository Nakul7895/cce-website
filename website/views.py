import datetime
from random import shuffle
import random
from django.shortcuts import render
from website.models import *
from django.http import Http404, HttpResponse
from django.core import serializers


def home_page(request):
    """
    This function is used to render the home page of the website.
    :param request: The request that is sent to the server.
    :return: The rendered html file of the home page.
    """
    if request.method == "GET":
        anouncement = HomeAnouncement.objects.all().first()
        testimonials = Testimonials.objects.all()
        updates = HomeUpdates.objects.all()
        events = HomeEvents.objects.all().order_by("?")
        gallery_imgs = Gallery.objects.all().order_by("?")[:20]
        upcomingEvents = UpcomingEvents.objects.all().order_by("?")[:6]
        recruiters = Recruiters.objects.all()
        recruiters3 = recruiters.order_by("?")
        recruiters2 = recruiters.order_by("?")
        achivements = Achivements.objects.order_by("?")
        image_urls = gallery_imgs[:6]
        gallery_data = Gallery.objects.all().order_by("?")[:20]
        context = {
            "anouncement": anouncement,
            "Testimonials": testimonials,
            "updates": updates,
            "Events": events,
            "gallery": gallery_imgs,
            "imgs":image_urls,
            'gallery_data': gallery_data,
            "upcomingEvents": upcomingEvents,
            "recruiters": recruiters,
            "recruiters2": recruiters2,
            "recruiters3": recruiters3,
            "achivements": achivements,
        }
        return render(request, "home.html", context=context)


def events_page(request):
    events = UpcomingEvents.objects.all()[::-1]
    hero_img = Hero_Image.objects.all().filter(page="events").first()
    hero_title = "Events"
    gallery_imgs = Gallery.objects.all().order_by("?")[:6]
    context = {"events" : events, "hero_img": hero_img, "hero_title": hero_title,"gallery": gallery_imgs}

    return render(request, "Events.html", context=context)


def admission_page(request):
    hero_img = Hero_Image.objects.all().filter(page="admissions").first()
    hero_title = "Admission"
    return render(request, "admission.html",context={"hero_img":hero_img,"hero_title":hero_title})

def admission_stat_page(request):
    hero_img = Hero_Image.objects.all().filter(page="admissions").first()
    hero_title = "Admission Statistics"
    years = [year[0] for year in AdmissionStatistics.objects.values_list('year').distinct()]
    context_temp = {"hero_img":hero_img,"hero_title":hero_title,"years":years}
    if request.method == "GET":
        yr = request.GET.get("year")
        if yr:
            table = AdmissionStatistics.objects.all().filter(year = yr)
            graph = AdmissionGraph.objects.all().filter(year = yr)
            context = {**context_temp,"table":table,"graph":graph,"year":yr}
        else:
            table = AdmissionStatistics.objects.all().filter(year = years[0])
            graph = AdmissionGraph.objects.all().filter(year = years[0])
            context = {**context_temp,"table":table,"graph":graph,"year":years[0]}
        return render(request, 'admission_stats.html',context=context)    
    else:
        return Http404("Page Not Found")

def nirf_page(request):
    return render(request, "nirf.html", context={})

def nba_page(request):
    return render(request, "nba.html", context={})


def gallery_page(request):
    if request.method == "GET":
        if request.GET.get("dep"):
            department = request.GET.get("dep")
            if department == "ALL":
                gallery_imgs = Gallery.objects.all().order_by("?")
                if gallery_imgs:
                    context = {"gallery": gallery_imgs, "dep": department}
                    return render(request, "gallery.html", context=context)
            else:
                gallery_imgs = Gallery.objects.filter(department=department)
                if gallery_imgs:
                    context = {"gallery": gallery_imgs, "dep": department}
                    return render(request, "gallery.html", context=context)
        else:
            gallery_imgs = Gallery.objects.all().order_by("?")
            if gallery_imgs:
                context = {"gallery": gallery_imgs}
                return render(request, "gallery.html", context=context)
            else:
                return render(request, "gallery.html", {"error": "No images found"})
    return render(
        request, "gallery.html", {"error": "No images found", "dep": department}
    )


def alumini_page(request):
    return render(request, "Alumini.html")


def facilities_page(request):
    """Displays the facilities page"""
    facilities = Facilities.objects.all()
    hero_img = Hero_Image.objects.all().filter(page="facilities").first()
    hero_title = "Facilities"
    context = {"facilities": facilities, "hero_img": hero_img, "hero_title": hero_title}
    return render(request, "facilities.html", context)


def research_page(request, slug):
    hero_img = Hero_Image.objects.all().filter(page="research").first()
    updates = HomeUpdates.objects.all()
    context_temp = {"hero_img": hero_img, "slug": slug, "updates": updates}

    match slug:
        case "index":
            hero_title = "Research"
            context = {"hero_title": hero_title, **context_temp}

            return render(request, "researchAndConsultancy/index.html", context)
        case "consultancy":
            context = {
                "hero_title": "Academic Consultancy",
                "academic_consultancy": AcademicConsultancy.objects.all(),
                **context_temp,
            }
            return render(
                request, "researchAndConsultancy/academic_consultancy.html", context
            )
        case "parternship":
            context = {
                "hero_title": "Academic Partnership",
                "academic_partnership": AcademicPartnerShip.objects.all(),
                **context_temp,
            }
            return render(
                request, "researchAndConsultancy/academic_partnership.html", context
            )
        case "conference":
            context = {
                **context_temp,
                "hero_title": "Conference & Symposium ",
                "conferences": Conference.objects.all(),
            }
            return render(request, "researchAndConsultancy/conference.html", context)
        case "funded_projects":
            hero_title = "Funded Projects"

            cse_projects = FundedProjects.objects.all().filter(department="CSE")
            ece_projects = FundedProjects.objects.all().filter(department="ECE")
            eee_projects = FundedProjects.objects.all().filter(department="EEE")
            me_projects = FundedProjects.objects.all().filter(department="ME")
            ce_projects = FundedProjects.objects.all().filter(department="CE")
            bsh_projects = FundedProjects.objects.all().filter(department="BSH")
            context = {
                "cse_projects": cse_projects,
                "ece_projects": ece_projects,
                "eee_projects": eee_projects,
                "me_projects": me_projects,
                "ce_projects": ce_projects,
                "bsh_projects": bsh_projects,
                "hero_title": hero_title,
                **context_temp,
            }
            return render(
                request, "researchAndConsultancy/funded_projects.html", context
            )
        case "publications":
            publications = FacultyStudentPublications.objects.all()
            context = {
                **context_temp,
                "hero_title": "Publications",
                "publications": publications,
            }
            return render(request, "researchAndConsultancy/publications.html", context)
        case "research_guides":
            research_guides = ResearchGuides.objects.all()
            context = {
                **context_temp,
                "hero_title": "KTU Approved RESEARCH GUIDES",
                "research_guides": research_guides,
            }

            return render(
                request, "researchAndConsultancy/research_guides.html", context
            )
        case other:
            raise Http404("Page Kanumanilla")


def test_page(request):
    return render(request, "Test.html")


def server_error_page(request):
    return render(request, "Errors/500.html",status=500)


def not_found_error_page(request, exception):

    return render(request, "Errors/404.html",status=404)
