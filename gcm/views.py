from django.utils.translation import ugettext_lazy as _

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FormParser,JSONParser

from .models import Device
from .serializers import DeviceSerialzer


class GCMListRegister(APIView):
    parser_classes = (FormParser,JSONParser,)

    def post(self, request, format=None):
        serializer = DeviceSerialzer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


        else:
            if(Device.objects.filter(dev_id=request.DATA['dev_id']).count()==1):
                object = Device.objects.get(dev_id=request.DATA['dev_id'])
                object.reg_id=request.DATA['reg_id']
                object.is_active=True
                object.save()

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class GCMListUnRegister(APIView):
    parser_classes = (FormParser,JSONParser,)
    def post(self, request, format=None):
        serializer = DeviceSerialzer(data=request.DATA)
        if serializer.is_valid():
            try:
                object = Device.objects.get(reg_id=request.DATA['reg_id'],dev_id=request.DATA['dev_id'])
                object.is_active=False
                object.save()
            except Device.DoesNotExist:
                return Response(_("This Device Doesn't Exist"),status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
