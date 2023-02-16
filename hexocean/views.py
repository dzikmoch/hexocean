from .models import Image
from .serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets

class ImageView(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def list(self, request):
        query_set = Image.objects.all().filter(user=request.user)
        serializer = ImageSerializer(query_set, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            query_set = Image.objects.all().filter(user=request.user)
            serializer = ImageSerializer(query_set, many=True, context={"request": request})
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

