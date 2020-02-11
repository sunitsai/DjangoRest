from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register(r'teacher',views.TeacherViewset,basename="Teacher")
router.register(r'student',views.StudentViewset,basename="Student")