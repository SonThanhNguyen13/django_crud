import json
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DataTable
from .form import DataForm
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated


class Index(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'Info': "Hello"})


class DataList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = DataTable.objects.all()
        serializer = DataForm(instance=data, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        return Response({'Error': 'Post not allowed'})

class SearchData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            data = DataTable.objects.get(id=pk)
            serializer = DataForm(instance=data, many=False)
            return Response({'Data': serializer.data})
        except ObjectDoesNotExist:
            return Response({'Error': "Object does not exists"})

    def post(self, request):
        return Response({'Error': 'Post not allowed'})

class UpdateData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'Error': 'Get not allowed'})

    def post(self, request):
        update_data = json.loads(request.body)
        try:
            data = DataTable.objects.get(id=update_data['id'])
            serializer = DataForm(instance=data, data = update_data)
            if serializer.is_valid():
                return Response({'Info': 'Successfully updated'})
            else:
                return Response({'Error': 'Invalid data'})
        except ObjectDoesNotExist:
            return Response({"Error": "Object does not exists"})


class CreateData(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'Error': 'Get not allowed'})

    def post(self, request):
        create_data = json.loads(request.body)
        serializer = DataForm(data=create_data)
        if serializer.is_valid():
            return Response({'Info': 'Created Successfully'})
        else:
            return Response({'Error':'Invalid data'})


class Delete(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'Error': 'Get not allowed'})

    def delete(self, request, pk):
        try:
            data = DataTable.objects.get(id=pk)
            data.delete()
            return Response({'Info': "Deleted Successfully"})
        except ObjectDoesNotExist:
            return Response({'Error': 'Object does not exits'})

    def post(self, request):
        return Response({'Error': 'Get not allowed'})