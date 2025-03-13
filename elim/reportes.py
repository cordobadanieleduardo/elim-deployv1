import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils import timezone
from django.db.models import Avg, Max, Min,Sum,Count
from .models import Registro
import datetime
from django.db.models import TextField
from django.db.models import OuterRef,Subquery
from django.db.models.functions import JSONObject
from django.contrib.postgres.expressions import ArraySubquery

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(f'media URI must start with {sUrl} or {mUrl}')
    return path

def reporte_registros(request):
    template_path = 'reportes/repo_print_all.html'
    
    # newest = Registro.objects.filter(fecha=OuterRef("pk")).order_by("-fecha")
    # Registro.objects.annotate(newest_commenter_email=Subquery(newest.values("email")[:1]))
    
    year=2025
    month=3
    dayi=1
    dayf=31
    inicio = datetime.datetime( year=year, month=month, day=dayi, tzinfo=None)
    final = datetime.datetime( year=year, month=month, day=dayf, hour=23, minute=59, second=59, tzinfo=None)
    sql = f'''select id, placa_id, 
    coalesce(count(id),0) as cantidad,
    coalesce(sum(valor),0.0) as valor,
    coalesce(sum(efectivo),0.0) as efectivo,
    coalesce(sum(transferencia),0.0) as transferencia,
    coalesce(sum(credito),0.0) as credito 
    from elim_registro 
    where fecha between '{inicio}' and '{final}'
    and estado = 1 
    group by placa_id order by 4 desc'''
    reg = Registro.objects.raw(sql)    
    print('++++',reg.query)
    today = timezone.now()
    context = {
        'obj': reg,
        'today': today,
        'request': request
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse(f'Error <pre> {html}</pre>')
    return response


# def imprimir_compra(request, compra_id):
#     template_path = 'cmp/compras_print_one.html'
#     today = timezone.now()
    
#     enc = Registro.objects.filter(id=compra_id).first()
#     if enc:
#         detalle = ComprasDet.objects.filter(compra__id=compra_id)
#     else:
#         detalle={}

    
#     context = {
#         'detalle': detalle,
#         'encabezado':enc,
#         'today':today,
#         'request': request
#     }
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

#     # create a pdf
#     pisaStatus = pisa.CreatePDF(
#        html, dest=response, link_callback=link_callback)
#     # if error then show some funy view
#     if pisaStatus.err:
#        return HttpResponse('We had some errors <pre>' + html + '</pre>')
#     return response


