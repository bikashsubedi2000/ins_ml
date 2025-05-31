# model_app/ml_predictor.py
MODEL_FEATURE_ORDER = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

# model_app/ml_predictor.py
import joblib
import os
from django.conf import settings

# This list defines the order of features expected by your model
MODEL_FEATURE_ORDER = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

# Construct the absolute path to the model file
MODEL_PATH = os.path.join(settings.BASE_DIR, 'model_app', 'ml_models', 'model_joblib_gr') # RENAME your_model_name.pkl

try:
    model = joblib.load(MODEL_PATH)
    print(f"Model loaded successfully from {MODEL_PATH}")
except FileNotFoundError:
    model = None
    print(f"ERROR: Model file not found at {MODEL_PATH}. Please check the path and filename.")
except Exception as e:
    model = None
    print(f"Error loading model: {e}")

def make_prediction(input_features_dict):
    """
    Makes a prediction using the loaded model.
    input_features_dict: A dictionary where keys are feature names (e.g., 'age', 'bmi')
                         and values are the feature values.
    Returns the prediction.
    """
    if model is None:
        raise Exception("Model not loaded. Check server logs and model path.")

    try:
        # 1. Create a list of feature values in the correct order
        feature_values = [input_features_dict[feature_name] for feature_name in MODEL_FEATURE_ORDER]
        
        # 2. The model (e.g., scikit-learn) typically expects a 2D list/array for predictions,
        #    even for a single sample. So, [[val1, val2, ...]].
        model_input = [feature_values]
        
        # 3. Make the prediction
        prediction = model.predict(model_input)
        
        # 4. Post-process prediction if necessary
        #    (e.g., if model.predict returns an array like [result], get result)
        #    This handles cases where prediction might be a list/tuple or a direct value.
        if isinstance(prediction, (list, tuple)) and len(prediction) > 0:
            return prediction[0] 
        return prediction

    except KeyError as e:
        raise ValueError(f"Missing feature in input: {str(e)}. Expected all of: {MODEL_FEATURE_ORDER}")
    except Exception as e:
        # Log the full error for debugging, then raise a more user-friendly one or the same
        print(f"Error during prediction with input {input_features_dict}: {str(e)}")
        raise Exception(f"Error during model prediction process: {str(e)}")