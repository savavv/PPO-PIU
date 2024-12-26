# intermediate_software/views.py

import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

logger = logging.getLogger(__name__)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'time': openapi.Schema(type=openapi.TYPE_INTEGER, description='GPS время в наносекундах'),
            'packetType': openapi.Schema(type=openapi.TYPE_INTEGER, description='Тип команды'),
            'deviceID': openapi.Schema(type=openapi.TYPE_INTEGER, description='Идентификатор устройства'),
            'deviceType': openapi.Schema(type=openapi.TYPE_INTEGER, description='Тип устройства'),
            'deviceLatitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Широта устройства'),
            'deviceLongitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Долгота устройства'),
            'deviceAltitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Высота устройства'),
            'signalType': openapi.Schema(type=openapi.TYPE_INTEGER, description='Тип радиосигнала'),
            'signalFrequency': openapi.Schema(type=openapi.TYPE_INTEGER, description='Частота сигнала в Гц'),
            'signalAmplitude': openapi.Schema(type=openapi.TYPE_INTEGER, description='Амплитуда сигнала'),
            'signalWidth': openapi.Schema(type=openapi.TYPE_INTEGER, description='Ширина сигнала в Гц'),
            'signalDetectionType': openapi.Schema(type=openapi.TYPE_INTEGER, description='Тип обнаружения'),
            'uav': openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'uavType': openapi.Schema(type=openapi.TYPE_STRING, description='Тип БПЛА'),
                    'serialNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Серийный номер БПЛА'),
                    'startUavLatitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Широта старта БПЛА'),
                    'startUavLongitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Долгота старта БПЛА'),
                    'uavLatitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Текущая широта БПЛА'),
                    'uavLongitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Текущая долгота БПЛА'),
                    'uavAltitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Текущая высота БПЛА'),
                    'operatorLatitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Широта оператора БПЛА'),
                    'operatorLongitude': openapi.Schema(type=openapi.TYPE_NUMBER, description='Долгота оператора БПЛА')
                }
            )
        },
        required=['time', 'packetType', 'deviceID', 'deviceType', 
                  'deviceLatitude', 'deviceLongitude', 'deviceAltitude',
                  'signalType', 'signalFrequency', 'signalAmplitude',
                  'signalWidth', 'signalDetectionType']  
    ),
    responses={201: openapi.Response('Success', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={'status': openapi.Schema(type=openapi.TYPE_STRING)}
    ))}
)
@csrf_exempt  
@api_view(['POST'])
def api_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.info(f"Получено от ПИУ: {data}")

            # Логика обработки данных...
            response_data = {"status": "success"}
            logger.info(f"Отправлено обратно ПИУ: {response_data}")  
            return JsonResponse(response_data, status=201)

        except json.JSONDecodeError:
            logger.error("Ошибка декодирования JSON")
            return JsonResponse({"status": "error", "message": "Invalid JSON received"}, status=400)

    return JsonResponse({"status": "ok"}, status=200)
