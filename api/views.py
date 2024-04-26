from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EventOrder
from .serializers import EventOrderSerializer


# Create your views here.
class EventOrderListCreate(generics.ListCreateAPIView):
    queryset = EventOrder.objects.all()
    serializer_class = EventOrderSerializer


class EventOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventOrder.objects.all()
    serializer_class = EventOrderSerializer
    lookup_field = 'pk'


class EventOrderList(APIView):

    def get(self, request, format=None):  # type: ignore # noqa : A002
        title = request.query_params.get('title', None)

        if title:
            event_order = EventOrder.objects.filter(title=title)
        else:
            event_order = EventOrder.objects.all()

        serializer = EventOrderSerializer(event_order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
