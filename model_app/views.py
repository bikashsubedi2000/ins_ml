from django.shortcuts import render
from .forms import InsurancePredictionForm
from .ml_predictor import make_prediction # Import the prediction function

def prediction_input_view(request):
    prediction_result = None
    error_message = None
    form = InsurancePredictionForm() # Instantiate the form

    if request.method == 'POST':
        form = InsurancePredictionForm(request.POST)
        if form.is_valid():
            try:
                # form.cleaned_data is a dictionary of validated input
                # e.g., {'age': 40, 'sex': 1, 'bmi': 40.3, ...}
                input_data_dict = form.cleaned_data
                prediction_result = make_prediction(input_data_dict)
            except Exception as e:
                error_message = f"Prediction error: {str(e)}"
                # You might want to log the full traceback here for debugging
                print(f"Error in prediction_input_view: {e}")
        else:
            # Form is not valid, errors will be displayed by the form in the template
            error_message = "Please correct the errors below."


    context = {
        'form': form,
        'prediction': prediction_result,
        'error_message': error_message,
    }
    return render(request, 'model_app/predict_page.html', context)