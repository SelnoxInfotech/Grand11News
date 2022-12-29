from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Category,SubCategory,News,VideoNews
from .serializer import Serializer_Category,Serializer_SubCategory,Serializer_News,Serializer_Videonews




#Category Api
class GetCategories(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            User = Category.objects.select_related().all()
            serialize = Serializer_Category(User, many=True)
            
            return Response(serialize.data)
        except Exception as e:
            return Response({'error' : str(e)},status=500)
    
    
    
    
class AddCategories(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = Serializer_Category(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success","data": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)
        except Exception as e:
            return Response({'error' : str(e)},status=500)

class UpdateCategories(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, id=None):
        try:
            User = Category.objects.get(id=id)
            serializer = Serializer_Category(User, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(modified_by=request.user.username)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)
        except Exception as e:
            return Response({'error' : str(e)},status=500)

class DeleteCategory(APIView):
    # permission_classes = [IsAuthenticated]

    def delete(self, request, id=None):
        try:
            User = get_object_or_404(Category, id=id)
            User.delete()
            return Response({"status": "success", "data": "Deleted"})
        except Exception as e:
            return Response({'error' : str(e)},status=500)
 
 
#Sub Category Api
class GetSubCategories(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            User = SubCategory.objects.select_related().all()
            serialize = Serializer_SubCategory(User, many=True)
            # categoryName=Category.objects.filter()
            # for i in categoryName:
            #     print(i)
            return Response({"data":serialize.data},status=200)
        except Exception as e:
            return Response({'error' : str(e)},status=500)

class AddSubCategories(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = Serializer_SubCategory(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success","data": serializer.data}, status=200)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)
        except Exception as e:
            return Response({'error' : str(e)},status=500)


class UpdateSubCategories(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, id=None):
        try:
            User = SubCategory.objects.get(id=id)
            serializer = Serializer_SubCategory(User, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(modified_by=request.user.username)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)
        except Exception as e:
            return Response({'error' : str(e)},status=500)


class DeleteSubCategory(APIView):
    # permission_classes = [IsAuthenticated]

    def delete(self, request, id=None):
        try:
            User = get_object_or_404(SubCategory, id=id)
            User.delete()
            return Response({"status": "success", "data": "Deleted"})
        except Exception as e:
            return Response({'error' : str(e)},status=500)
        
        
#News
class GetNews(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            User = News.objects.select_related().all()
            serialize = Serializer_News(User, many=True)
            return Response(serialize.data)
        except Exception as e:
            return Response({'error' : str(e)},status=500)
    
class AddNews(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = Serializer_News(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success","data": serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)
        except Exception as e:
            return Response({'error' : str(e)},status=500)


class UpdateNews(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, id=None):
        try:
            User = News.objects.get(id=id)
            serializer = Serializer_News(User, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(modified_by=request.user.username)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)
        except Exception as e:
            return Response({'error' : str(e)},status=500)


class DeleteNews(APIView): 
    # permission_classes = [IsAuthenticated]
    
    def delete(self, request, id=None):
        try:
            User = get_object_or_404(News, id=id)
            User.delete()
            return Response({"status": "success", "data": "Deleted"})
        except Exception as e:
            return Response({'error' : str(e)},status=500)    


#Video News  
class GetVideoNews(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        try:
            User = VideoNews.objects.select_related().all()
            serialize = Serializer_Videonews(User, many=True)
            # categoryName=Category.objects.filter()
            # for i in categoryName:
            #     print(i)
            return Response({"data":serialize.data},status=200)
        except Exception as e:
            return Response({'error' : str(e)},status=500)

class AddVideoNews(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = Serializer_Videonews(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success","data": serializer.data}, status=200)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)
        except Exception as e:
            return Response({'error' : str(e)},status=500)


class UpdateVideoNews(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, id=None):
        try:
            User = VideoNews.objects.get(id=id)
            serializer = Serializer_Videonews(User, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(modified_by=request.user.username)
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors},status=400)
        except Exception as e:
            return Response({'error' : str(e)},status=500)


class DeleteVideoNews(APIView):
    # permission_classes = [IsAuthenticated]

    def delete(self, request, id=None):
        try:
            User = get_object_or_404(VideoNews, id=id)
            User.delete()
            return Response({"status": "success", "data": "Deleted"})
        except Exception as e:
            return Response({'error' : str(e)},status=500)
 