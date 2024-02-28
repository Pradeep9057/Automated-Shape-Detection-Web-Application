# Automated Shape Detection Web Application

This web application allows users to upload images and perform automated shape detection using computer vision algorithms. Users can choose between detecting circles or rectangles in the uploaded images. The application is built using the Flask framework for the backend and OpenCV library for image processing.

## Features

- User-friendly interface for uploading images and selecting detection options.
- Detection of circles using OpenCV's SimpleBlobDetector.
- Detection of rectangles using contour detection algorithms.
- Display of processed images with detected shapes back to the user.
- Secure file upload functionality to prevent common security vulnerabilities.

## Installation

To run the application locally, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/automated-shape-detection.git
   
1. Install the required Python dependencies:
    pip install -r requirements.txt

2. Run the Flask application:
    python Pipe_App.py
   
3. Access the application in your web browser at http://localhost:5000

## Usage
Upload an image using the file input field.
Select the desired shape detection option (circles or rectangles) using radio buttons.
Click the "Submit" button to process the uploaded image.
The processed image with detected shapes will be displayed on the output page.
Project Structure
Pipe_App.py: Main Flask application file containing routes and logic.
my_module.py: Module containing shape detection functions.
templates/: Directory containing HTML templates for the web application.
images5/: Directory to store uploaded images.
Dependencies
Flask: Web framework for Python.
OpenCV: Computer vision library for image processing.
numpy: Library for numerical computations in Python.
Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
https://github.com/Pradeep9057/Automated-Shape-Detection-Web-Application.git
