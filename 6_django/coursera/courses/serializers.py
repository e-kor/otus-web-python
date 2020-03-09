from rest_framework import serializers

from courses.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(write_only=False, required=False)

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'description', 'date')


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    tutor_name = serializers.StringRelatedField(read_only=True,
                                                source='tutor')

    class Meta:
        model = Course
        fields = (
            'id', 'name', 'description', 'tutor_name', 'is_active', 'lessons')

    def update(self, instance, validated_data):
        lessons_data = validated_data.pop("lessons")
        for lesson_data in lessons_data:
            lesson_id = lesson_data.pop('id', 0)
            if lesson_id:
                Lesson.objects.filter(pk=lesson_id).update(**lessons_data)
            else:
                Lesson.objects.create(course=instance, **lesson_data)
        for attr_name, value in validated_data.items():
            setattr(instance, attr_name, value)
        instance.save()
        return instance

    def create(self, validated_data):
        lessons_data = validated_data.pop("lessons", [])
        instance = Course.objects.create(**validated_data)
        Lesson.objects.bulk_create(
            [Lesson(course=instance, **data) for data in lessons_data])
        return instance
