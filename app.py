from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    nama, IPS = [x for x in request.form.values()]

    data = []

    data.append(int(char))
    if Nama == '':
        data.extend([0, 1])
    else:
        data.extend([1, 0])

    if IPS == 'Ya':
        data.extend([0, 1])
    else:
        data.extend([1, 0])
        
    
    
    prediction = model.predict([data])
    output = round(prediction[0], 2)

    return render_template('index.html', insurance_cost=output, Nama=nama, IPS=IPS)


if __name__ == '__main__':
    app.run(debug=True)