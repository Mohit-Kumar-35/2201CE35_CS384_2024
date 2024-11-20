from flask import Flask, request, send_file, render_template
import pandas as pd
from io import BytesIO
import tut10  # Import the Python processing code

app = Flask(__name__)

# Serve the HTML upload form
@app.route('/')
def index():
    return render_template('upload.html')

# Handle the file upload and call the Python code
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    # Process the uploaded file using your Python code
    output_file = tut10.process_excel(file)

    # Return the processed file to the user
    return send_file(output_file, as_attachment=True, download_name='Processed_Output.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    app.run(debug=True)
