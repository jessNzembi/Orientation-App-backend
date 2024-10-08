from django.urls import path
from .views import HODList, HODDetail, CourseList, CourseDetail, hodsdetails_view

urlpatterns = [
    path('hods/', HODList.as_view(), name='hod-list'),
    path('hods/<int:pk>/', HODDetail.as_view(), name='hod-detail'),
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<str:name>/', CourseDetail.as_view(), name='course-detail'),
    path('course-detail/', hodsdetails_view, name='courses_details'),
]
