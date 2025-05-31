# model_app/forms.py
from django import forms

class InsurancePredictionForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=0, help_text="Enter your age.")
    # For ChoiceField, if your choices values are already the target type (int here),
    # Django usually handles it. Remove coerce.
    sex = forms.ChoiceField(
        label='Sex',
        choices=[(1, 'Male'), (0, 'Female')],
        # coerce=int, # <--- REMOVE THIS LINE
        help_text="Select your sex."
    )
    bmi = forms.FloatField(label='BMI', min_value=0.0, help_text="Enter your Body Mass Index.")
    children = forms.IntegerField(label='Number of Children', min_value=0, help_text="How many children do you have?")
    smoker = forms.ChoiceField(
        label='Smoker',
        choices=[(1, 'Yes'), (0, 'No')],
        # coerce=int, # <--- REMOVE THIS LINE
        help_text="Are you a smoker?"
    )
    region = forms.ChoiceField(
        label='Region',
        choices=[(0, 'NorthEast'), (1, 'NorthWest'), (2, 'SouthEast'), (3, 'SouthWest')],
        # coerce=int, # <--- REMOVE THIS LINE
        help_text="Select your region."
    )