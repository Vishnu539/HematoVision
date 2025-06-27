# HematoVision: Advanced Blood Cell Classification

HematoVision is a deep learning-based web application that classifies different types of white blood cells from microscopic images. It leverages a custom Convolutional Neural Network (CNN) trained using transfer learning techniques to deliver accurate predictions with a user-friendly interface.

---

## 🚀 Features

* Classifies four types of white blood cells:

  * Eosinophils
  * Lymphocytes
  * Monocytes
  * Neutrophils
* Custom CNN model with over 15M parameters
* Achieved 83%+ test accuracy
* Real-time image upload and prediction via web app
* Performance visualizations (loss & accuracy plots)
* Clean, modern, and responsive UI

---

## 🧠 Model Overview

* **Architecture:** Custom-built CNN with multiple convolutional blocks, batch normalization, and dropout layers
* **Input Shape:** 224x224x3
* **Training:**

  * Optimizer: SGD with LR scheduler
  * Loss Function: Categorical Crossentropy
  * Epochs: 20 (with EarlyStopping)
  * Data Augmentation: rotation, zoom, shift, flip, etc.
* **Performance:**

  * Test Accuracy: **\~83%**
  * F1-scores for each class provided in the classification report

---

## 📁 Project Structure

```
HematoVision/
├── app.py
├── saved_model/
│   └── blood_cell_improved.h5
├── static/
│   ├── css/
│   │   └── styles.css
│   └── uploads/
├── templates/
│   ├── home.html
│   └── result.html
├── requirements.txt
└── README.md
```

---

## 💻 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/HematoVision.git
cd HematoVision
```

2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

4. Open browser and go to `http://127.0.0.1:5000/`

---

## 📊 Sample Prediction Output

* Prediction result page shows:

  * Uploaded image
  * Predicted class name
  * Informative description of the blood cell type

---

## 📎 Dependencies

* TensorFlow / Keras
* Flask
* NumPy, Pillow
* Bootstrap 5

---

## 📚 Acknowledgements

* Microscopic Blood Cell Dataset sourced from open-access medical repositories
* Project developed for academic submission
* Special thanks to the project mentor(s) and contributors

---

## 📌 Future Work

* Deploy app on Render / HuggingFace Spaces
* Improve model generalization with more data
* Add support for additional cell types

---

## 📃 License

This project is for academic and research purposes only.
