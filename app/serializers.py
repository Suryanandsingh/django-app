from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = ('owner', 'type', 'source_type', 'source_id', 'input_meta_data')
