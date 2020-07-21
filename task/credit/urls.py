from django.urls import path, include
from credit.views import MakeRequestView


app_name = 'credit'


urlpatterns = [
    path('request/create/', MakeRequestView.as_view()),
]
