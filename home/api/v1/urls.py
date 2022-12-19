from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    AppViewSet,
    PlanViewSet,
    SubViewSet
    
)

router = DefaultRouter()
#router.register("signup", SignupViewSet, basename="signup")
#router.register("logins", LoginViewSet, basename="login")
router.register("app", AppViewSet, basename="app")
router.register("plans", PlanViewSet, basename="plans")
router.register("subs", SubViewSet, basename="subs")

urlpatterns = [
    path("", include(router.urls)),
]
