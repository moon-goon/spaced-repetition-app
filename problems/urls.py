from rest_framework import routers
from .api import ProblemViewSet

router = routers.DefaultRouter()
router.register('api/problems', ProblemViewSet, 'problems')

urlpatterns = router.urls
