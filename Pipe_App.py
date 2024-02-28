from flask import Flask, render_template, request,send_from_directory
from my_module import detect_circles
from my_module import detect_rectangles
import os.path
import os
import cv2
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024

@app.route("/output", methods=["POST"])
def home():
    target = os.path.join(APP_ROOT, 'images5/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
    execution_path = target
    print(execution_path)
        # Check which radio button is selected
    selected_option = request.form.get("Pipes-Bars")
    
    if selected_option == "Pipes":
        # Detect circles for pipes
        image = detect_circles(os.path.join(execution_path, filename))
        out_image = cv2.imwrite(os.path.join(execution_path,  "out_"+filename), image)

    else:
         image = detect_rectangles(destination)
         out_image = cv2.imwrite(os.path.join(execution_path,  "out_"+filename), image)
    return render_template("OUTPUT.html", image_name="out_" + filename)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images5", filename)


if __name__ == "__main__":
    app.run(debug=True)