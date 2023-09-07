from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict_package():
    cgpa = float(request.form.get('cgpa'))

    # prediction
    result = model.predict(np.array([cgpa]).reshape(1, 1))

    package = float(result)

    package = format(package, ".2f")

    output = "placed with a package of " + str(package)

    return render_template('index.html', result=output)


if __name__ == 'main':
    app.run(host='0.0.0.0',port=8080)
