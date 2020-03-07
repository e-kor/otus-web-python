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
            if lesson_data.get('id'):
                l = Lesson.objects.get(pk=lesson_data.pop('id'))
                for attr_name, value in lesson_data.items():
                    setattr(l, attr_name, value)
            else:
                l = Lesson(**lesson_data)
                l.course = instance
            l.save()
        for attr_name, value in validated_data.items():
            setattr(instance, attr_name, value)
        instance.save()
        return instance

    def create(self, validated_data):
        lessons_data = validated_data.pop("lessons", [])
        instance = Course.objects.create(**validated_data)
        for lesson_data in lessons_data:
            l = Lesson(**lesson_data)
            l.course = instance
            l.save()
        return instance
