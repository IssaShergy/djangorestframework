from django.urls import include, path
from rest_framework.routers import DefaultRouter
from profiles.api.views import   ProfileViewSet,ProfileStatusViewSet,AvatarUpdateView
from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register("profiels",ProfileList)
                                 

router = DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet ,basename="status")
# profile_list=ProfileList.as_view({"get":"list"})
# profile_detail=ProfileList.as_view({"get":"retrieve"})
urlpatterns = [
    path("",include(router.urls) ),
    # path("profiles/", profile_list,name="profile-list"),
    # path("profiles/<int:pk>", profile_detail,name="profile-detail"),
    # path("", include(router.urls)),
    path("avatar/", AvatarUpdateView.as_view(), name="avatar-update")
]