from rest_framework import serializers
from . import models
from drf_extra_fields.fields import Base64ImageField

class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		extra_kwargs = {
			'email': {'write_only': True}
		}
		fields = (
				'id',
				'course',
				'name',
				'email',
				'review',
				'rating',
				'created_at'
			)
		model = models.Review

class CourseSerializer(serializers.ModelSerializer):
	class Meta:
		fields = (
				'id',
				'title',
				'url'
			)
		model = models.Course

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
                'id',
                'imageUri',
                'logo',
                'color',
                'label',
                'text',
                'status'
        )
        model = models.ImageInfo