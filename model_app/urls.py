from django.urls import path
from . import views

app_name = 'model_app' # Good practice for namespacing
urlpatterns = [
    path('', views.prediction_input_view, name='predict_insurance'),
]