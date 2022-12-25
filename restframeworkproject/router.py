from apiapp.viewset import UserViewset
from apiapp.viewset import ClientViewset
from apiapp.viewset import ProjectViewset
from rest_framework import routers


router =  routers.DefaultRouter()
router.register('user',UserViewset)
router.register('client',ClientViewset)
router.register('project',ProjectViewset)