from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import (Domain, Csv, Images, Template, configTemplate)
from .trash import pre
import dns.resolver
import requests
from bs4 import BeautifulSoup
from .utils import solvequery, renderer, dynamicdata
import json
import pandas as pd
import io
import pprint
import random
import ast


class headCount(): # this just counts the number of objects in every templates app model, this just for showing data in sub navbar component of page
    def __init__(self):
        self.pg = Template.objects.count()
        self.tm = Template.objects.count()
        self.dm = Domain.objects.count()
        self.file = Csv.objects.count()
        self.folder = Images.objects.count()


def templates(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        type = request.POST.get('type')
        if type == 'delete':
            Template.objects.filter(publicID=id).delete()
            return JsonResponse({'type': type, "status": "deleted"})

    payload = Template.objects.all()
    return render(request, 'templates/templates.html', {"data": payload, "headcounts": headCount()})


def templates_add(request):
    if request.method == 'POST':
        tpName = request.POST.get('tpName')
        domain = request.POST.get('domain')
        csvName = request.POST.get('csvName')
        folderName = request.POST.get('folderName')

        try:
            csv_info = Csv.objects.filter(csvName=csvName).first()
            folder_info = Images.objects.filter(folder=folderName).first()

            tp2DB = Template(name=tpName, folder=folder_info,
                             file=csv_info)
            tp2DB.save()
            domain_info = Domain.objects.filter(
                domain=domain).update(site=tp2DB)
            tpconfig = configTemplate(template=tp2DB, id=tp2DB.publicID)
            tpconfig.save()
            return redirect("..")

        except:
            pass

    return render(request, 'templates/templates_add.html')


def templates_detail(request, id): # preview of the rendered index page by using the json generated in templates_generate function
    try:
        data = configTemplate.objects.filter(
            id=id).first()
        payload = json.loads(data.renderedjson)
        imgs = ast.literal_eval(data.template.folder.imgLinks)
        Dynamic = dynamicdata(payload)

        return render(request, 'templates/templates_detail.html', {'staticdata': payload, "cred": data, "imgs": imgs, "dynamic": Dynamic})

    except:
        return HttpResponse("error: 404")


def settings(request):   # accepting post request from templates/settings
    if request.method == "POST":
        id = request.get_full_path().split("=")[1]
        bName = request.POST.get('bName')
        bLogo = request.POST.get('bLogo')
        bHead = request.POST.get('bHead')
        bDesc = request.POST.get('bDesc')
        bLocation = request.POST.get('bLocation')
        bSite = request.POST.get('bSite')
        bCTA = request.POST.get('bCTA')
        bMail = request.POST.get('bMail')
        bPhone = request.POST.get('bPhone')
        configTemplate.objects.filter(id=id).update(
            bName=bName, bLogo=bLogo, bHead=bHead, bDesc=bDesc, bLocation=bLocation, bSite=bSite, bCTA=bCTA, bMail=bMail, bPhone=bPhone)
        print("somewhat done")

        return redirect("..")

    if request.GET.get('id'):  # posting data to template/settings for getting previously filled data from the form
        id = request.GET.get('id')

        payload = configTemplate.objects.filter(id=id).first()
        return render(request, 'templates/templates_settings.html', {'data': payload, })

    return redirect("..")


def templates_generate(request):  # this function accepts post request data from templates/generate section -> then uses pandas(from utlis.py) for filtering data from csv
    if request.method == "POST":
        id = request.POST.get("id")
        generate = configTemplate.objects.filter(id=id).first()
        rawcsv = requests.get(generate.template.file.csvUrl).text
        csv = pd.read_csv(io.StringIO(rawcsv), sep=',')
        rendered = renderer(csv, request.POST) # a function trying to create structured json from the request and map it with the csv data :) try not use it because it doesn't fit with the kenefit project concepts
        renderedjson = json.dumps(rendered)
        rawjson = json.dumps(request.POST)
        id = request.GET.get("id")
        configTemplate.objects.filter(id=id).update(
            rawjson=rawjson, renderedjson=renderedjson)

        return redirect("..")

    id = request.GET.get("id")
    payload = configTemplate.objects.filter(id=id).first()
    try:
        ren = json.loads(payload.renderedjson)
        pre = json.loads(payload.rawjson)
    except:
        ren = ""
        pre = ""
    return render(request, 'templates/templates_generate.html', {"data": payload, "pre": pre, "render": ren})


def domains(request):
    payload = Domain.objects.all()
    return render(request, 'templates/templates_domains.html', {"data": payload, "headcounts": headCount()})


def obtain_cname(username, domname):
    hostname = domname
    Cname = '%s.%s.kenefit.com' % (domname, username)
    return hostname, Cname


def domains_add(request):
    return render(request, 'templates/templates_domains_add.html')


def verify_cname(hostname): #this function verifies the domain whether it is connected to our subdomains or not
    try:
        re = dns.resolver.query(hostname, 'CNAME')
        for val in re:
            e = val.target
        return str(e)

    except Exception as e:
        return "No Record Found"


@csrf_exempt
def domains_verify(request):
    if request.method == "POST":
        subdomain_name = request.POST.get("subName")
        domain_url = request.POST.get("urlName")
        current_user = "Sahil".lower()
        name, cname = obtain_cname(current_user, subdomain_name)
        registerDomain = Domain(host_name=name, cname=cname.lower(
        ), domain=f"{subdomain_name}.{domain_url}")
        registerDomain.save()
        return render(request, 'templates/templates_domains_verify.html', {'cname': cname, 'host_name': name, 'urlName': f"{subdomain_name}.{domain_url}"})

        # adding to Domains Model

    #     # current_user = get_object_or_404(User, pk=request.user.pk)
    #     hostname, Cname = obtain_cname(domname, current_user.username)
    #     client = Clients.objects.get(user=current_user)
    #     c = str(client)

    # # Restrict Based On Plan
    #     p = ''
    #     p1 = "Platform"
    #     p2 = "Enterprice"
    #     p3 = "Business"
    #     if p1 in c:
    #         p = "Platform"
    #         x = 2
    #     elif p2 in c:
    #         p = "Enterprice"
    #         x = 8
    #     elif p3 in c:
    #         p = "Business"
    #         x = 4

    #     domains = Domain.objects.filter(user=current_user).order_by('-created')
    #     if(p and domains.count() <= x):
    #         print(hostname, Cname)
    #         result = verify_cname('mail.google.com')
    #         print(result)
    #         if(result == Cname):
    #             if request.method == 'POST':
    #                 form = HostForm(data=request.POST)
    #                 if form.is_valid():
    #                     host_name = request.POST.get("host_name")
    #                     cname = request.POST.get("cname")
    #                 # update Domain model for the current_user
    #                     new_domain = Domain()
    #                     new_domain.host_name = host_name
    #                     new_domain.cname = cname
    #                     new_domain.user = current_user
    #                     new_domain.save()

    #                     return redirect('account')
    #                 else:
    #                     logger.info("Verification Failed")
    #                     return print('failed verification')

    #             else:
    #                 form = HostForm()
    #         else:
    #             return render(request, 'verify.html', {'cname': Cname, 'host_name': hostname, 'alert_flag': True})
    #     else:
    #         return render(request, 'verify.html', {'limit_flag': True})

    #     return render(request, 'verify.html', {'cname': Cname, 'host_name': hostname})
    elif request.method == "GET":
        Cname = request.GET.get("cname").lower()
        url = request.GET.get("urlName").lower()
        result = verify_cname(url)[:-1]
        print(Cname, result)
        if Cname == result:
            Domain.objects.filter(cname=Cname).update(status=True)
        return redirect("..")

    else:
        return render(request, 'templates/templates_domains_add.html')


@csrf_exempt
def files(request): 
    if request.method == "POST":
        type = request.POST.get("type")
        # type = "delete"
        id = request.POST.get("id").split("^^^^")
        realName = id[0]
        realUrl = id[-1]
        if type == "refresh":
            response = requests.get(realUrl)
            csvNumRows = len(response.text.split("\n")) - 1
            Csv.objects.filter(csvUrl=realUrl, csvName=realName).update(
                csvRows=csvNumRows)
            return JsonResponse({'type': type, "row": csvNumRows})

        elif type == "delete":
            Csv.objects.filter(givenUrl=realUrl, csvName=realName).delete()
            return JsonResponse({'type': type, "status": "deleted"})

    payload = Csv.objects.all()
    return render(request, 'templates/templates_files.html', {"data": payload, "headcounts": headCount()})


@csrf_exempt
def files_add(request): # this functions deals with uploading and getting rows of the csv file. I have used requests & bs4 libraries to fetch content of csv file
    if request.method == "POST":
        fName = request.POST.get("fName")
        fUrl = request.POST.get("fUrl")
        if "drive.google.com" in fUrl:  # Checking whether its drive link or not
            csvID = fUrl.split("/")[-2]
            csvUrl = f"https://drive.google.com/uc?id={csvID}&export=download"
        elif "dropbox.com" in fUrl:   # operation if the file is from dropbox
            csvUrl = f"{fUrl[:-1]}1"
        else:
            csvUrl = fUrl
        csvNumRows = 0
        try:
            response = requests.get(csvUrl)
            csvNumRows = len(response.text.split("\n")) - 1

        except:
            return render(request, 'templates/templates_files_add.html')

        csv2DB = Csv(csvName=fName, csvUrl=csvUrl,
                     csvRows=csvNumRows, givenUrl=fUrl)
        csv2DB.save()
        return redirect("..")
    return render(request, 'templates/templates_files_add.html')


@csrf_exempt
def folders(request): 
    if request.method == "POST":     #updating and getting standalone links of every image in the uploaded folder by the it only works with google drive. I have again used requests & bs4 libraries to fetch content of folder
        type = request.POST.get("type")
        # type = "delete"
        id = request.POST.get("id").split("^^^^")
        folder = id[0]
        Url = id[-1]
        if type == "refresh":
            try:
                raw = requests.get(Url)
                html = BeautifulSoup(raw.text, "html.parser")
                img_list = html.select("c-data")
                imgArr = []
                for i in img_list[1:-7]:
                    x = i["jsdata"].split(";")[3]
                    imgArr.append(
                        f"https://lh3.googleusercontent.com/u/0/d/{x}")

                folder2DB = Images.objects.filter(Url=Url, folder=folder).update(
                    imgLinks=str(imgArr), numImg=len(imgArr))
                return JsonResponse({'type': type, "status": "updated"})

            except:
                pass

        elif type == "delete":
            Images.objects.filter(Url=Url, folder=folder).delete()
            return JsonResponse({'type': type, "status": "deleted"})
    payload = Images.objects.all()
    return render(request, 'templates/templates_folders.html', {"data": payload,  "headcounts": headCount()})


@csrf_exempt
def folders_add(request):   # this functions deals with uploading and getting standalone links of every image in the uploaded folder by the it only works with google drive. I have again used requests & bs4 libraries to fetch content of folder
    if request.method == "POST":
        folder = request.POST.get("folder")
        url = request.POST.get("url")
        try:
            raw = requests.get(url)
            html = BeautifulSoup(raw.text, "html.parser")
            movie_list = html.select("c-data")
            imgArr = []
            for i in movie_list[1:-7]:
                x = i["jsdata"].split(";")[3]
                imgArr.append(f"https://lh3.googleusercontent.com/u/0/d/{x}")

            folder2DB = Images(folder=folder, Url=url,
                               imgLinks=str(imgArr), numImg=len(imgArr))
            folder2DB.save()

        except:
            return render(request, 'templates/templates_folders_add.html')
        return redirect("..")
    return render(request, 'templates/templates_folders_add.html')


def plans(request):
    return render(request, 'templates/templates_plans.html')


def plans_checkout(request):
    return render(request, 'templates/templates_plans_checkout.html')


def plans_checkout_failed(request):
    return render(request, 'templates/templates_plans_checkout_failed.html')


def plans_checkout_passed(request):
    return render(request, 'templates/templates_plans_checkout_passed.html')
