from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from search_backend.serializers import VideoDataSerializer
from search_backend.models import VideoData

# Create your views here.

class VideoDataListView(ListAPIView):
    
    queryset = VideoData.objects.all().order_by("publish_datetime")
    serializer_class = VideoDataSerializer
    pagination_class = PageNumberPagination


class SearchVideView(ListAPIView):

    serializer_class = VideoDataSerializer
    pagination_class = PageNumberPagination
    
    def get(self, request):

        try:
            search_query = request.GET.get("query", None)
            if not search_query:
                return Response({"status": "FAILED", "message": "search query not provided"}, status=status.HTTP_400_BAD_REQUEST)
        
            videos_query_set = VideoData.objects.all().order_by("publish_datetime")
            search_results = videos_query_set.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query)).all()

            page = self.paginate_queryset(search_results)
            if page:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)


            serializer = self.get_serializer(search_results, many=True)
            return Response({"status": "SUCCESS", "data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "FAILED", "message": f"some error occured : {e}"}, status=status.HTTP_200_OK)
        