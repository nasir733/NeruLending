from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *

urlpatterns = [

    path('token/', TokenObtainPairPatchedView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('user/get_user_info/', GetUserByToken.as_view(), name='get_user_info'),
    path('user/fetch_personal_data/', FetchPersonalData.as_view(), name='fetch_personal_data'),
    path('user/register/', RegisterNewUserAPI.as_view(), name='register_new_user'),

]
