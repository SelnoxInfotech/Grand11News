from django.urls import path
from .views import *



urlpatterns = [
    path('Add-Category/', AddCategories.as_view()),
    path('Get-Category/', GetCategories.as_view()),
    path('update-Category/<int:id>', UpdateCategories.as_view()),
    path('delete-Category/<int:id>', DeleteCategory.as_view()),
    ###################################################################################################
    path('Add-SubCategory/', AddSubCategories.as_view()),
    path('Get-SubCategory/', GetSubCategories.as_view()),
    path('update-SubCategory/<int:id>', UpdateSubCategories.as_view()),
    path('delete-SubCategory/<int:id>', DeleteSubCategory.as_view()),
    #####################################################################################################
    path('Add-News/', AddNews.as_view()),
    path('Get-News/', GetNews.as_view()),
    path('update-News/<int:id>', UpdateNews.as_view()),
    path('delete-News/<int:id>', DeleteNews.as_view()),
    #####################################################################################################
    path('Add-VideoNews/', AddVideoNews.as_view()),
    path('Get-VideoNews/', GetVideoNews.as_view()),
    path('update-VideoNews/<int:id>', UpdateVideoNews.as_view()),
    path('delete-VideoNews/<int:id>', DeleteVideoNews.as_view()),


]        