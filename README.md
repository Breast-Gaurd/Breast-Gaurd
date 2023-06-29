# Breast Cancer Prediction Model :woman_health_worker:
Project Demo Video Link : [Click Here](https://drive.google.com/file/d/1BGsK8Qe3ud7cBlkgTcaMllTJrbcLLOMn/view?usp=drive_link)<br>
Project Report:  [Click Here](https://drive.google.com/file/d/1YJ-CgGW3kHXYTeOKarRyk6IEnYYpmdjx/view?usp=sharing)

This repository contains a machine learning model for predicting breast cancer. The model utilizes a dataset of measurements related to breast tumor characteristics and provides predictions on whether the tumor is cancerous or non-cancerous.

## Model Details :microscope:

The breast cancer prediction model is built using Python and the Flask web framework. It employs a machine learning algorithm trained on a labeled dataset of breast tumor measurements. The model takes into account various features such as radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension.

The trained model is serialized using the pickle library and stored in the `model1.pkl` file.

## Usage :rocket:

To use the breast cancer prediction model, follow the steps below:

1. Clone the repository:  :open_file_folder::
```
git clone https://github.com/your-username/breast-cancer-prediction.git
```
2. Install the required dependencies: :package::
```
pip install -r requirements.txt
```
4. Run the Flask web application: :computer::


5. Open your web browser and visit `http://localhost:5000` to access the prediction interface.

6. Enter the required measurement data in the provided form and submit it.

7. The model will process the input and display the predicted result, indicating whether the tumor is cancerous or non-cancerous.

Feel free to modify the `app.py` file and the HTML templates in the `templates` directory to customize the user interface or incorporate additional functionality.

## Repository Structure :file_folder:

The repository is structured as follows:
```
breast-cancer-prediction/
├── app.py
├── model1.pkl
├── templates/
│ ├── index.html
└── README.md
```

- `app.py`: Contains the Flask application code, including the routes for handling user requests and making predictions using the trained model.
- `model1.pkl`: Serialized machine learning model saved as a pickle file.
- `templates/`: Directory containing HTML templates for the web interface.
- `README.md`: This readme file providing information about the project.

## Contributing :handshake:

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.



You are encouraged to use this model responsibly and consult with medical professionals for accurate diagnosis and treatment decisions.




