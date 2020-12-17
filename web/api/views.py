import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DataTable
from .form import DataForm
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class Index(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'Info': "Hello"})


class DataList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = DataTable.objects.all()
        serializer = DataForm(instance=data, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        create_data = json.loads(request.body)
        serializer = DataForm(data=create_data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Info': 'Created Successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Error': 'Invalid data'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class DataDetail(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            del_data = DataTable.objects.get(id=pk)
            del_data.delete()
            data = DataTable.objects.all()
            serializer = DataForm(instance=data, many=True)
            return Response({'data':serializer.data}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            content = {"Error":"Object does not exist"}
            return Response(content=content, status = status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            data = DataTable.objects.get(id=pk)
            update_data = json.loads(request.body)
            serializer = DataForm(instance=data, data=update_data)
            if serializer.is_valid():
                serializer.save()
                data = DataTable.objects.all()
                serializer = DataForm(instance=data, many=True)
                return Response({'data': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'Error': 'Invalid data'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except ObjectDoesNotExist:
            return Response({'Error': 'Invalid data'}, status=status.HTTP_404_NOT_FOUND)
