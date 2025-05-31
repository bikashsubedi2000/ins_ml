from django import forms

class InsurancePredictionForm(forms.Form):
    age = forms.IntegerField(label='Age', min_value=0, help_text="Enter your age.")
    
    sex = forms.ChoiceField(
        label='Sex',
        choices=[(1, 'Male'), (0, 'Female')],
        help_text="Select your sex."
    )

    bmi = forms.FloatField(label='BMI', min_value=0.0, help_text="Enter your Body Mass Index.")

    children = forms.IntegerField(label='Number of Children', min_value=0, help_text="How many children do you have?")

    smoker = forms.ChoiceField(
        label='Smoker',
        choices=[(1, 'Yes'), (0, 'No')],
        help_text="Are you a smoker?"
    )

    region = forms.ChoiceField(
        label='Region',
        choices=[(0, 'NorthEast'), (1, 'NorthWest'), (2, 'SouthEast'), (3, 'SouthWest')],
        help_text="Select your region."
    )

    # 🔍 Validate BMI to ensure it is within a realistic range
    def clean_bmi(self):
        bmi = self.cleaned_data['bmi']
        if bmi < 10 or bmi > 60:
            raise forms.ValidationError("BMI should be between 10 and 60.")
        return bmi

    # 🔍 Validate age
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 1 or age > 120:
            raise forms.ValidationError("Age must be between 1 and 120.")
        return age

    # 🔍 Overall validation if needed
    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get('age')
        bmi = cleaned_data.get('bmi')
        smoker = cleaned_data.get('smoker')

        # Example of inter-field validation
        if smoker == '1' and bmi is not None and bmi > 40:
            self.add_error('bmi', "Smokers with BMI over 40 are at extreme risk.")
