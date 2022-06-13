#this page deals with the multi tenant feature of the kenefit
# for making use of it you have to make wildcard dns record 
#  hostname    value
#         *        your server ip    
# get reference from https://www.namecheap.com/support/knowledgebase/article.aspx/597/2237/how-can-i-set-up-a-catchall-wildcard-subdomain/


from django.shortcuts import render, HttpResponse
from templates.models import Template, configTemplate, Domain
from templates.utils import dynamicdata
import json
import ast


def routing(request):
    domain = request.get_host()
    if domain == "kenefit.com":
        return HttpResponse("kenefit's Landing page")

    else:
        try:
            print("sssssss")
            root = Domain.objects.filter(domain=domain).first()
            id = root.site.publicID
            data = configTemplate.objects.filter(
                id=id).first()
            print(data,"111")
            payload = json.loads(data.renderedjson)
            imgs = ast.literal_eval(data.template.folder.imgLinks)
            Dynamic = dynamicdata(payload)
            return render(request, 'templates/templates_detail.html', {'staticdata': payload, "cred": data, "imgs": imgs, "dynamic": Dynamic})

        except:
            return HttpResponse("error: 404")


def paths(request, slug):
    domain = request.get_host()
    root = Domain.objects.filter(domain=domain).first()
    id = root.site.publicID
    data = configTemplate.objects.filter(
        id=id).first()
    payload = json.loads(data.renderedjson)
    imgs = ast.literal_eval(data.template.folder.imgLinks)
    Dynamic = dynamicdata(payload)
    slugs = [payload["topic1"], payload["topic2"], payload["topic3"],
             payload["topic4"], payload["topic5"], payload["product"]]
    change = {}
    for i in slugs:
        if slug.lower() == i["slug"].lower():
            change["title"] = i["title"]
            change["description"] = i["blockdescription"]
            change["metatitle"] = i["metatitle"]
            break

    if change == {}:
        return HttpResponse("error: 404")
    return render(request, 'templates/templates_detail.html', {"changes": change, 'staticdata': payload, "cred": data, "imgs": imgs, "dynamic": Dynamic})
