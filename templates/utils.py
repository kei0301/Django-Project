# this file deals with convertion templates/generate form data to a structured json

import json
import pandas as pd
import io
import random

# just don't use this function as it is not the functionality what kennefit project wants
def solvequery(csv, str, query=""): # this function deals with managing queries and csv variables with pandas
    try:
        df = csv

    except:
        pass

    if str[0] != "$":
        return str, None

    elif str[0] == "$":
        output = str.split("=")[0].replace(" ", '')[1:]  # removing spaces
        ourquery = []
        if (str.split("=")) != 1:
            ourquery = str.split("=")[-1].split(";")
        queryArr = []
        if query != "":
            queryArr.append(query)
        txtArr_before = []
        txtArr_after = []
        for param in ourquery:
            paramquery = param
            if paramquery == '':
                continue
            if paramquery[0] == "$":
                type = 'query'

            else:
                type = 'str'
                txt = param.split("::")[0]
                position = param.split("::")[-1].replace(" ", "")
                if position == "before":
                    txtArr_before.append(txt)

                elif position == "after":
                    txtArr_after.append(txt)

            if type == 'query':
                col = paramquery[1:].split("{")[0].split("(")[0]
                key = paramquery.split(
                    "{")[-1].split("(")[-1].split("}")[0].split(")")[0]
                typeof = None
                if "{" in paramquery and "}" in paramquery:
                    typeof = "value"

                elif "(" in paramquery and ")" in paramquery:
                    typeof = "btw"

                if typeof == "value":
                    qstr = f"{col} == '{key}'"
                    queryArr.append(qstr)

                elif typeof == "btw":
                    v_arr = key.split(",")
                    if v_arr[-1] in [">", "<"]:
                        qstr = f"{col} {v_arr[-1]} {v_arr[0]}"
                        queryArr.append(qstr)

                    else:
                        qstr = f"{col} > {v_arr[0]} and {col} < {v_arr[-1]}"
                        queryArr.append(qstr)

        else:

            querystr = " and ".join(queryArr)
            before = " ".join(txtArr_before)
            after = " ".join(txtArr_after)

            # print(querystr, before, after, sep="\n")
            if querystr != "":
                load = df.query(querystr, inplace=False)

            else:
                load = df

            data = [f"{before} {i} {after}" for i in load[output]]
            return data, querystr

def renderer(csv, payload):

    rendered = {}
    rendered["index"] = {"title": payload.get(
        'indexTitle'), "description": payload.get('indexDesc')}
    rendered["value"] = {"title": payload.get('valueTitle'), "description": payload.get('valueDesc'), "values": [payload.get(
        'value01Title'), payload.get('value02Title'), payload.get('value03Title'), payload.get('value04Title')]}
    # topic1
    rendered["topic1"] = {"title": payload.get('topic01BlockTitle'), "blockdescription": payload.get('topic01BlockDescription'), "metatitle": payload.get(
        'topic01Title'), "slug": payload.get('topic01Slug'), "breadcrumb": payload.get('topic01Breadcrumb')}
    tp1Name, query = solvequery(csv, payload.get('topic01Name'))
    tp1label, query2 = solvequery(
        csv, payload.get('topic01Label'), query)
    tp1desc, query2 = solvequery(
        csv, payload.get('topic01Description'), query)

    tpArr = []
    for i in range(len(tp1Name)):
        dict = {"name": tp1Name[i], "label": tp1label[i],
                "description": tp1desc[i]}
        tpArr.append(dict)

    rendered["topic1"]["cards"] = tpArr

    # topic2
    rendered["topic2"] = {"title": payload.get('topic02BlockTitle'), "blockdescription": payload.get('topic02BlockDescription'), "metatitle": payload.get(
        'topic02Title'), "slug": payload.get('topic02Slug'), "breadcrumb": payload.get('topic02Breadcrumb')}
    tp2Name, query = solvequery(csv, payload.get('topic02Name'))
    tp2label, query2 = solvequery(
        csv, payload.get('topic02Label'), query)
    tp2desc, query2 = solvequery(
        csv, payload.get('topic02Description'), query)

    tpArr = []
    for i in range(len(tp2Name)):
        dict = {"name": tp2Name[i], "label": tp2label[i],
                "description": tp2desc[i]}
        tpArr.append(dict)

    rendered["topic2"]["cards"] = tpArr

    # topic3
    rendered["topic3"] = {"title": payload.get('topic03BlockTitle'), "blockdescription": payload.get('topic03BlockDescription'), "metatitle": payload.get(
        'topic03Title'), "slug": payload.get('topic03Slug'), "breadcrumb": payload.get('topic03Breadcrumb')}
    tp3Name, query = solvequery(csv, payload.get('topic03Name'))
    tp3label, query2 = solvequery(
        csv, payload.get('topic03Label'), query)
    tp3desc, query2 = solvequery(
        csv, payload.get('topic03Description'), query)

    tpArr = []
    for i in range(len(tp3Name)):
        dict = {"name": tp3Name[i], "label": tp3label[i],
                "description": tp3desc[i]}
        tpArr.append(dict)

    rendered["topic3"]["cards"] = tpArr

    # topic4
    rendered["topic4"] = {"title": payload.get('topic04BlockTitle'), "blockdescription": payload.get('topic04BlockDescription'), "metatitle": payload.get(
        'topic04Title'), "slug": payload.get('topic04Slug'), "breadcrumb": payload.get('topic04Breadcrumb')}
    tp4Name, query = solvequery(csv, payload.get('topic04Name'))
    tp4label, query2 = solvequery(
        csv, payload.get('topic04Label'), query)
    tp4desc, query2 = solvequery(
        csv, payload.get('topic04Description'), query)

    tpArr = []
    for i in range(len(tp4Name)):
        dict = {"name": tp4Name[i], "label": tp4label[i],
                "description": tp4desc[i]}
        tpArr.append(dict)

    rendered["topic4"]["cards"] = tpArr

    # topic5
    rendered["topic5"] = {"title": payload.get('topic05BlockTitle'), "blockdescription": payload.get('topic05BlockDescription'), "metatitle": payload.get(
        'topic05Title'), "slug": payload.get('topic05Slug'), "breadcrumb": payload.get('topic05Breadcrumb')}
    tp5Name, query = solvequery(csv, payload.get('topic05Name'))
    tp5label, query2 = solvequery(
        csv, payload.get('topic05Label'), query)
    tp5desc, query2 = solvequery(
        csv, payload.get('topic05Description'), query)

    tpArr = []
    for i in range(len(tp5Name)):
        dict = {"name": tp5Name[i], "label": tp5label[i],
                "description": tp5desc[i]}
        tpArr.append(dict)

    rendered["topic5"]["cards"] = tpArr

    # product
    rendered["product"] = {"title": payload.get('productBlockTitle'), "blockdescription": payload.get('productBlockDescription'), "metatitle": payload.get(
        'productTitle'), "slug": payload.get('productSlug'), "breadcrumb": payload.get('productBreadcrumb')}
    pdtName, query = solvequery(csv, payload.get('productName'))
    pdtlabel, query2 = solvequery(
        csv, payload.get('productLabel'), query)
    pdtdesc, query2 = solvequery(
        csv, payload.get('productDescription'), query)

    tpArr = []
    for i in range(len(pdtName)):
        dict = {"name": pdtName[i], "label": pdtlabel[i],
                "description": pdtdesc[i]}
        tpArr.append(dict)

    rendered["product"]["cards"] = tpArr

    # packages
    rendered["packages"] = {"title": payload.get(
        'packageBlockTitle'), "description": payload.get('packageBlockDescription'), "productButtonCta": payload.get('productButtonCta'), "productButtonRedirect": payload.get('productButtonRedirect')}

    # faq
    rendered["faq"] = {"title": payload.get(
        'faqBlockTitle'), "description": payload.get('faqBlockDescription')}
    faqArr = []
    for i in range(int(payload.get('faqnum'))):
        dict = {}
        dict["q"] = payload.get(f'faqTitle{i+1}')
        dict["ans"] = payload.get(f'faqCustomerName{i+1}')
        dict["customer"] = payload.get(f'faqDescription{i+1}')
        faqArr.append(dict)

    rendered["faq"]["q_a"] = faqArr

    # solutions
    rendered["solutions"] = {"title": payload.get(
        'solutionBlockTitle'), "description": payload.get('solutionBlockDescription')}
    solArr = []
    for i in range(int(payload.get('solnum'))):
        dict = {}
        dict["q"] = payload.get(f'solutiontitle{i+1}')
        dict["customer"] = payload.get(f'solutionlabel{i+1}')
        dict["ans"] = payload.get(f'solutiondescription{i+1}')
        solArr.append(dict)

    rendered["solutions"]["arr"] = solArr

    rendered["interlink"] = {"title": payload.get('interlinkTestimonial'), "interlink01Title": payload.get("interlink01Title"), "interlink02Title": payload.get("interlink02Title"), "interlink03Title": payload.get(
        "interlink03Title"), "interlink04Title": payload.get("interlink04Title"), "interlink05Title": payload.get("interlink05Title"), "interlink06Title": payload.get("interlink06Title"), }
    plArr = []
    for i in range(int(payload.get('peoplenum'))):
        dict = {}
        dict["name"] = payload.get(f'Customer{i+1}')
        dict["location"] = payload.get(f'Location{i+1}')
        plArr.append(dict)

    rendered["interlink"]["testimonial"] = plArr

    return rendered


def dynamicdata(payload):
    Dynamic = {}
    Dynamic["tp1"] = {1: payload['topic1']['cards']
                      [random.randint(0, len(payload['topic1']['cards']) - 1)],
                      2: payload['topic1']['cards']
                      [random.randint(0, len(payload['topic1']['cards']) - 1)],
                      3: payload['topic1']['cards']
                      [random.randint(0, len(payload['topic1']['cards']) - 1)],
                      4: payload['topic1']['cards']
                      [random.randint(0, len(payload['topic1']['cards']) - 1)],
                      }

    Dynamic["tp2"] = {1: payload['topic2']['cards']
                      [random.randint(0, len(payload['topic2']['cards']) - 1)],
                      2: payload['topic2']['cards']
                      [random.randint(0, len(payload['topic2']['cards']) - 1)],
                      3: payload['topic2']['cards']
                      [random.randint(0, len(payload['topic2']['cards']) - 1)],
                      4: payload['topic2']['cards']
                      [random.randint(0, len(payload['topic2']['cards']) - 1)],
                      5: payload['topic2']['cards']
                      [random.randint(0, len(payload['topic2']['cards']) - 1)],
                      6: payload['topic2']['cards']
                      [random.randint(0, len(payload['topic2']['cards']) - 1)], }

    Dynamic["tp3"] = {1: payload['topic3']['cards']
                      [random.randint(0, len(payload['topic3']['cards']) - 1)],
                      2: payload['topic3']['cards']
                      [random.randint(0, len(payload['topic3']['cards']) - 1)],
                      3: payload['topic3']['cards']
                      [random.randint(0, len(payload['topic3']['cards']) - 1)],
                      4: payload['topic3']['cards']
                      [random.randint(0, len(payload['topic3']['cards']) - 1)],
                      5: payload['topic3']['cards']
                      [random.randint(0, len(payload['topic3']['cards']) - 1)],
                      6: payload['topic3']['cards']
                      [random.randint(0, len(payload['topic3']['cards']) - 1)], }

    Dynamic["tp4"] = {1: payload['topic4']['cards']
                      [random.randint(0, len(payload['topic4']['cards']) - 1)],
                      2: payload['topic4']['cards']
                      [random.randint(0, len(payload['topic4']['cards']) - 1)],
                      3: payload['topic4']['cards']
                      [random.randint(0, len(payload['topic4']['cards']) - 1)],
                      4: payload['topic4']['cards']
                      [random.randint(0, len(payload['topic4']['cards']) - 1)],
                      }

    Dynamic["tp5"] = {1: payload['topic5']['cards']
                      [random.randint(0, len(payload['topic5']['cards']) - 1)],
                      2: payload['topic5']['cards']
                      [random.randint(0, len(payload['topic5']['cards']) - 1)],
                      3: payload['topic5']['cards']
                      [random.randint(0, len(payload['topic5']['cards']) - 1)],
                      4: payload['topic5']['cards']
                      [random.randint(0, len(payload['topic5']['cards']) - 1)],
                      5: payload['topic5']['cards']
                      [random.randint(0, len(payload['topic5']['cards']) - 1)],
                      6: payload['topic5']['cards']
                      [random.randint(0, len(payload['topic5']['cards']) - 1)], }

    Dynamic["pdt"] = {1: payload['product']['cards']
                      [random.randint(
                          0, len(payload['product']['cards']) - 1)],
                      2: payload['product']['cards']
                      [random.randint(
                          0, len(payload['product']['cards']) - 1)],
                      3: payload['product']['cards']
                      [random.randint(
                          0, len(payload['product']['cards']) - 1)],
                      4: payload['product']['cards']
                      [random.randint(
                          0, len(payload['product']['cards']) - 1)],
                      5: payload['product']['cards']
                      [random.randint(
                          0, len(payload['product']['cards']) - 1)],
                      6: payload['product']['cards']
                      [random.randint(0, len(payload['product']['cards']) - 1)], }

    Dynamic["review"] = payload['interlink']['testimonial'][random.randint(
        0, len(payload['interlink']['testimonial']) - 1)]

    return Dynamic
