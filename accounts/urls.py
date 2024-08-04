from accounts.views import UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('accounts', UserViewSet)

urlpatterns = router.urls
from pprint import pprint
pprint(urlpatterns)