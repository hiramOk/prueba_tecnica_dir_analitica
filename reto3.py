from flask import Flask, jsonify, request, send_file
import pandas as pd

app = Flask(__name__)

@app.route('/post_csv', methods=['POST'])
def post_csv():
  if 'file' not in request.files:
    return "No se subio archivo"

  file = request.files['file']
  if file.filename == '':
    return 'No se seleccionó archivo'
  data = pd.read_csv(file)
  return data.to_json()

@app.route('/get_csv', methods=['POST'])
def get_csv():
  if 'file' not in request.files:
    return "No se subio archivo"

  file = request.files['file']
  if file.filename == '':
    return 'No se seleccionó archivo'
  data = pd.read_csv(file)
  return {'csv': data.to_string()}

@app.route('/get_json', methods=['POST'])
def get_json():
  if 'file' not in request.files:
    return "No se subio archivo"

  file = request.files['file']
  if file.filename == '':
    return 'No se seleccionó archivo'
  data = pd.read_csv(file)
  return {'json': data.to_string()}

if __name__ == '__main__':
  app.run(debug=True)