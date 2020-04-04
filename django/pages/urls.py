from django.urls import path

from .views import HomePageView, ByTagView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tags/<int:pk>/', ByTagView.as_view(), name='by_tag'),
]
