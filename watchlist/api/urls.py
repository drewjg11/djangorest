from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist.api.views import movies_list, movie_details
from watchlist.api.views import  ( WatchListAV, WatchDetailAV,
                                   StreamListAV, StreamDetailAV,
                                   ReviewList, ReviewDetail,
                                   ReviewCreate, StreamPlatformVS,
                                   UserReview, WatchListGV)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),
    path('new-list/', WatchListGV.as_view(), name='watch-detail'),

    path('', include(router.urls)),

    path('<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    path('reviews/', UserReview.as_view(), name='user-review-detail'),

    # path('streamlist/', StreamListAV.as_view(), name='stream-list'),
    # path('streamlist/<int:pk>', StreamDetailAV.as_view(), name='streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>', ReviewDetail.as_view(), name="review-detail"),
]
