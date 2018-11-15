import urllib.request as rq
import urllib.parse as parse
from urllib.error import HTTPError
import sys
import datetime

appId = 'AGNJ5BCN'
uids= 'UBX4D9LD,UQ2LWZNP,UYHQVXH9'
sitio = 'isfei.ddns.net:32400'
sitio = parse.quote(sitio)

fecha = datetime.datetime.now()
hora =  '<%s-%s-%s %s:%s> ' % (fecha.year, fecha.month, fecha.day, fecha.hour, fecha.minute)


mensaje = hora + sys.argv[1]
mensaje = parse.quote(mensaje)

url = "https://pushfleet.com/api/v1/send?appid=%s&userid=%s&message=%s&url=%s" % (appId, uids, mensaje, sitio)

cabeceras = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
request = rq.Request(url, headers=cabeceras)

try:
    respuesta = rq.urlopen(request)
    if respuesta.status == 200:
        print('Exito al enviar')
    else:
        print('Error de envio')
except HTTPError as error:
    print(error)
    print('Error de envio')
