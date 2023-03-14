from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
import time
import datetime
import sys
import importlib
import os

from backend.models import *


# Create your views here.

@require_http_methods(["GET"])
def show_data(request):
    date = request.GET.get('Date')
    repo = request.GET.get('Repo')
    repo1 = request.GET.get('repo')
    table_name = '' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    table_name_1 = 'Certificate' + repo1 + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[
        2] + ''
    table_name_2 = 'Roa' + repo1 + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    table_name_3 = 'AsnIp' + repo1 + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    models_name = importlib.import_module('backend.models')
    class_name = getattr(models_name, table_name)
    class_name_1 = getattr(models_name, table_name_1)
    class_name_2 = getattr(models_name, table_name_2)
    class_name_3 = getattr(models_name, table_name_3)
    response = {}
    try:
        dataset = class_name.objects.only('asn', 'ip_pre', 'max_len', 'not_before', 'not_after')[:100]
        ipb_num = class_name_3.objects.values('ip_block').count()
        asn_num = class_name_3.objects.values('asn').distinct().count()
        cert_num = class_name_1.objects.values('cert_uri').count()
        roa_num = class_name_2.objects.values('roa_uri').count()
        response['list'] = json.loads(serializers.serialize('json', dataset))
        response['msg'] = 'success'
        response['ip_block_number'] = str(ipb_num)
        response['asn_number'] = str(asn_num)
        response['cert_num'] = str(cert_num)
        response['roa_num'] = str(roa_num)
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_cert(request):
    date = request.GET.get('Date')
    ipb = request.GET.get('ipb')
    repo = request.GET.get('repo')
    table_name_1 = 'Certificate' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[
        2] + ''
    table_name_2 = 'Roa' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    table_name_3 = 'AsnIp' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    models_name = importlib.import_module('backend.models')
    class_name = getattr(models_name, table_name_1)
    class_name_2 = getattr(models_name, table_name_2)
    class_name_3 = getattr(models_name, table_name_3)
    response = {}
    try:
        roa_uri_object = class_name_3.objects.filter(ip_block=str(ipb)).only('roa_uri')
        roa_uri = str(roa_uri_object[0].roa_uri).split('(')[1].split(')')[0]
        roa_content = class_name_2.objects.filter(roa_uri=roa_uri).only('content')
        cert_uri_object = class_name_2.objects.filter(roa_uri=roa_uri).only('cert_uri')
        cert_uri = str(cert_uri_object[0].cert_uri).split('(')[1].split(')')[0]
        cert_content = class_name.objects.filter(cert_uri=cert_uri).only('content')
        response['cert'] = str(cert_content[0].content).split('-----BEGIN CERTIFICATE-----')[0]
        response['roa'] = str(roa_content[0].content)
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_data_1(request):
    date = request.GET.get('Date')
    repo = request.GET.get('Repo')
    repo_1 = request.GET.get('repo')
    table_name_1 = 'Certificate' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[
        2] + ''
    table_name_2 = 'Roa' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    table_name_3 = 'AsnIp' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    models_name = importlib.import_module('backend.models')
    class_name_1 = getattr(models_name, table_name_1)
    class_name_2 = getattr(models_name, table_name_2)
    class_name_3 = getattr(models_name, table_name_3)
    response = {}
    try:
        ipb_num = class_name_3.objects.values('ip_block').count()
        asn_num = class_name_3.objects.values('asn').distinct().count()
        cert_num = class_name_1.objects.values('cert_uri').count()
        roa_num = class_name_2.objects.values('roa_uri').count()
        asn_ip = class_name_3.objects.only('asn', 'ip_block', 'roa_uri')[:50]
        param = []
        routinator = []
        fp = open('/home/ken123456/Desktop/RPKI_ftp/routinator_' + date + '_' + repo_1 + '.txt', 'r')
        lines = fp.readlines()
        for line in lines:
            if 'Found' in line:
                routinator.append(line.split('\n')[0])
            if 'rsync' in line:
                routinator.append(line.split('\n')[0])
            if '   ' in line:
                routinator.append(line.split('\n')[0])
        fp.close()
        for i in range(50):
            roa_uri = str(asn_ip[i].roa_uri).split('(')[1].split(')')[0]
            cert_uri_object = class_name_2.objects.filter(roa_uri=roa_uri).only('cert_uri')
            cert_uri = str(cert_uri_object[0].cert_uri).split('(')[1].split(')')[0]
            param_1 = [asn_ip[i].asn, asn_ip[i].ip_block, roa_uri, cert_uri]
            param.append(param_1)
        # print(param)
        response['list'] = param
        response['routinator'] = routinator
        response['rout_len'] = len(routinator)
        response['msg'] = 'success'
        response['ip_block_number'] = str(ipb_num)
        response['asn_number'] = str(asn_num)
        response['cert_num'] = str(cert_num)
        response['roa_num'] = str(roa_num)
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def search_roa(request):
    date = request.GET.get('Date')
    repo = request.GET.get('Repo')
    ipb = request.GET.get('IP_block')
    table_name_2 = 'Roa' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    table_name_3 = 'AsnIp' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    models_name = importlib.import_module('backend.models')
    class_name_2 = getattr(models_name, table_name_2)
    class_name_3 = getattr(models_name, table_name_3)
    response = {}
    try:
        roa_uri_object = class_name_3.objects.filter(ip_block=str(ipb)).only('roa_uri')
        roa_uri = str(roa_uri_object[0].roa_uri).split('(')[1].split(')')[0]
        roa_content = class_name_2.objects.filter(roa_uri=roa_uri).only('content')
        response['roa'] = str(roa_content[0].content)
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def search_cert(request):
    date = request.GET.get('Date')
    repo = request.GET.get('Repo')
    roa_uri = request.GET.get('ROA_URI')
    table_name_1 = 'Certificate' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[
        2] + ''
    table_name_2 = 'Roa' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    models_name = importlib.import_module('backend.models')
    class_name_1 = getattr(models_name, table_name_1)
    class_name_2 = getattr(models_name, table_name_2)
    response = {}
    try:
        cert_uri_object = class_name_2.objects.filter(roa_uri=roa_uri).only('cert_uri')
        cert_uri = str(cert_uri_object[0].cert_uri).split('(')[1].split(')')[0]
        cert_content = class_name_1.objects.filter(cert_uri=cert_uri).only('content')
        response['cert'] = str(cert_content[0].content).split('-----BEGIN CERTIFICATE-----')[0]
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def search_auth(request):
    date = request.GET.get('Date')
    repo = request.GET.get('Repo')
    cert_uri = request.GET.get('Cert_URI')
    table_name_1 = 'Certificate' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[
        2] + ''
    models_name = importlib.import_module('backend.models')
    class_name_1 = getattr(models_name, table_name_1)
    response = {}
    try:
        auth_uri_object = class_name_1.objects.filter(cert_uri=cert_uri).only('auth_uri')
        auth_uri = str(auth_uri_object[0].auth_uri)
        auth_content = class_name_1.objects.filter(cert_uri=auth_uri).only('content')
        print(str(auth_content[0].content).split('-----BEGIN CERTIFICATE-----')[0])
        response['cert'] = str(auth_content[0].content).split('-----BEGIN CERTIFICATE-----')[0]
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def search(request):
    date = request.GET.get('Date')
    repo = request.GET.get('Repo')
    ip_block = request.GET.get('IP_block')
    table_name = '' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    models_name = importlib.import_module('backend.models')
    class_name = getattr(models_name, table_name)
    response = {}
    try:
        dataset = class_name.objects.filter(ip_pre=ip_block).only('asn', 'ip_pre', 'max_len', 'not_before', 'not_after')
        param = [dataset[0].asn, dataset[0].ip_pre, dataset[0].max_len, dataset[0].not_before, dataset[0].not_after]
        print(param)
        response['list'] = param
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def search_1(request):
    date = request.GET.get('Date')
    repo = request.GET.get('Repo')
    ip_block = request.GET.get('IP_block')
    table_name_2 = 'Roa' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    table_name_3 = 'AsnIp' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    models_name = importlib.import_module('backend.models')
    class_name_2 = getattr(models_name, table_name_2)
    class_name_3 = getattr(models_name, table_name_3)
    response = {}
    try:
        asn_ip_object = class_name_3.objects.filter(ip_block=ip_block).only('asn', 'ip_block', 'roa_uri')
        roa_uri = str(asn_ip_object[0].roa_uri).split('(')[1].split(')')[0]
        cert_uri_object = class_name_2.objects.filter(roa_uri=roa_uri).only('cert_uri')
        cert_uri = str(cert_uri_object[0].cert_uri).split('(')[1].split(')')[0]
        param = [asn_ip_object[0].asn, asn_ip_object[0].ip_block, roa_uri, cert_uri]
        response['list'] = param
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_rov(request):
    response = {}
    try:
        dataset = Rov.objects.all()[100:200]
        param = []
        for i in range(100):
            t1 = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(dataset[i].first_time))
            t2 = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(dataset[i].last_time))
            param_1 = [dataset[i].prefix, dataset[i].origin, dataset[i].type, dataset[i].result, dataset[i].reason, t1, t2]
            param.append(param_1)
        response['list'] = param
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def search_rov(request):
    ipb = request.GET.get('IP_block')
    response = {}
    try:
        data = Rov.objects.filter(prefix=ipb).all()
        t1 = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(data[0].first_time))
        t2 = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(data[0].last_time))
        param = [data[0].origin, data[0].prefix, data[0].type, data[0].result, data[0].reason, t1, t2]
        # print(param)
        response['list'] = param
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_link(request):
    ipb = request.GET.get('IP_block')
    repo = request.GET.get('Repo')
    date = request.GET.get('Date')
    response = {}
    table_name_1 = 'Certificate' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[
        2] + ''
    table_name_2 = 'Roa' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    table_name_3 = 'AsnIp' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    models_name = importlib.import_module('backend.models')
    class_name_1 = getattr(models_name, table_name_1)
    class_name_2 = getattr(models_name, table_name_2)
    class_name_3 = getattr(models_name, table_name_3)
    try:
        param = []
        auth_uri = ''
        asn_object = class_name_3.objects.filter(ip_block=str(ipb)).only('asn')
        roa_uri_object = class_name_3.objects.filter(ip_block=str(ipb)).only('roa_uri')
        roa_uri = str(roa_uri_object[0].roa_uri).split('(')[1].split(')')[0]
        param.append(roa_uri)
        cert_uri_object = class_name_2.objects.filter(roa_uri=roa_uri).only('cert_uri')
        cert_uri = str(cert_uri_object[0].cert_uri).split('(')[1].split(')')[0]
        param.append(cert_uri)
        while auth_uri != 'rsync://rpki.ripe.net/ta/ripe-ncc-ta.cer':
            auth_uri_object = class_name_1.objects.filter(cert_uri=cert_uri).only('auth_uri')
            auth_uri = str(auth_uri_object[0].auth_uri)
            cert_uri = auth_uri
            param.append(cert_uri)
        response['list'] = param
        response['length'] = len(param)
        response['asn'] = str(asn_object[0].asn)
        response['msg'] = 'success'
        # print(response)
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_content(request):
    response = {}
    uri = request.GET.get('URI')
    repo = request.GET.get('Repo')
    date = request.GET.get('Date')
    table_name_1 = 'Certificate' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[
        2] + ''
    table_name_2 = 'Roa' + repo + '' + date.split('-')[0] + '' + date.split('-')[1] + '' + date.split('-')[2] + ''
    models_name = importlib.import_module('backend.models')
    class_name_1 = getattr(models_name, table_name_1)
    class_name_2 = getattr(models_name, table_name_2)
    if uri == 'rsync://rpki.ripe.net/ta/ripe-ncc-ta.cer':
        os.system('openssl x509 -inform DER -in /home/ken123456/Desktop/RPKI_code/rpki_ripe_ta/ripe-ncc-ta.cer -text > 1.txt')
        f = open('1.txt', 'r')
        content = f.read().split('-----BEGIN CERTIFICATE-----')[0]
    elif '.roa' in uri:
        content_object = class_name_2.objects.filter(roa_uri=uri).only('content')
        content = str(content_object[0].content)
    else:
        content_object = class_name_1.objects.filter(cert_uri=uri).only('content')
        content = str(content_object[0].content).split('-----BEGIN CERTIFICATE-----')[0]
    try:
        response['content'] = content
        response['msg'] = 'success'
    except Exception as e:
        response['msg'] = str(e)
    return JsonResponse(response)