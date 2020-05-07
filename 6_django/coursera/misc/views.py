from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from courses.tasks import send_contact_mail


class FeedbackSerializer(serializers.Serializer):
    email = serializers.EmailField()
    body = serializers.CharField(max_length=1000)


@swagger_auto_schema(methods=['post'], request_body=FeedbackSerializer)
@api_view(['POST'])
def send_feedback(request: Request):
    serializer = FeedbackSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    send_contact_mail.send(**serializer.validated_data)
    return Response({"detail": "OK"})
