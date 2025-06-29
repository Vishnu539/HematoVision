from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# ✅ Load the improved trained model
model = load_model('blood_cell_improved.keras')

# Class labels
class_labels = ['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL']

# Cell type descriptions
cell_descriptions = {
    "EOSINOPHIL": "Eosinophils are a type of white blood cell involved in combating parasites and are also active during allergic reactions. They contain granules rich in enzymes that can be toxic to invaders. Elevated eosinophil levels are often seen in conditions like asthma, allergies, and parasitic infections. They usually make up about 1–4% of the white blood cells in the body. Their granules stain bright red or pink under the microscope.",

    "LYMPHOCYTE": "Lymphocytes are a subset of white blood cells central to the immune system. They include B cells, T cells, and natural killer cells, all of which help the body recognize and fight infections. High levels can indicate infections or chronic inflammation, while low levels might signal immune deficiencies. They appear with a large, dark-staining nucleus and scant cytoplasm.",

    "MONOCYTE": "Monocytes are the largest type of white blood cell and play a critical role in the immune system. They can differentiate into macrophages and dendritic cells to respond to pathogens. Monocytes help in phagocytosis (ingesting harmful particles) and antigen presentation. Their levels rise in chronic infections and inflammatory disorders. They have a large kidney-shaped nucleus.",

    "NEUTROPHIL": "Neutrophils are the most abundant white blood cells and act as the first responders during inflammation. They quickly migrate to sites of infection to engulf and destroy pathogens through phagocytosis. Neutrophils are crucial in the body's defense against bacteria. An increase in neutrophils often signals bacterial infections, while a decrease can indicate bone marrow issues or severe infections."
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400

    # Secure filename and save
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # ✅ Load and preprocess image (224x224 for improved model)
    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    # Make prediction
    prediction = model.predict(img_array)
    predicted_class = class_labels[np.argmax(prediction)]
    description = cell_descriptions.get(predicted_class, "No additional information available for the predicted cell type.")

    # Render result
    return render_template(
        'result.html',
        prediction=predicted_class,
        image_path=filepath,
        filename=filename,
        description=description
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7860)
