from rest_framework import status
from rest_framework.views import APIView
from rest_framework.reponse import Response

from .models import Document
from .serializers import DocumentSerializer

class DocumentView(APIView):
	def get_object(self, pk):
		try:
			return Document.objects.get(pk=pk)
		except Document.DoesNotExists:
			return Response('Invalid', status=status.HTTP_400_BAD_REQUEST)

	def get(self, request):
		queryset = self.get_object(pk)
		serializer_class = DocumentSerializer(queryset)
		return Response(serializer_class.data, status=status.HTTP_200_OK)

	def post(self, request, pk)
		serializer_class = DocumentSerializer(data=request.data)
		if serializer_class.is_valid():
			serializer_class.save()
			return Response(serializer_class.data, status=status.HTTP_201_CREATED)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		queryset = self.get_object(pk)
		queryset.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
