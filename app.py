from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
loaded_model = joblib.load("./model/calories_model.sav")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    gender = request.form.get('gender')
    age = float(request.form.get('age'))
    height = float(request.form.get('height') )
    weight = float(request.form.get('weight'))
    duration = float(request.form.get('duration'))
    heart_rate = float(request.form.get('heart_rate'))
    body_temperature = float(request.form.get('body_temp'))

    if gender == 'female':
        gender = 1.0;
    else:
        gender = 0.0;

    data = [[gender, age, height, weight, duration, heart_rate, body_temperature]]

    prediction = loaded_model.predict(data)[0]

    if prediction < 0:
        return render_template('index.html', prediction_text='Check Your Data Again')    
    else:
        return render_template('index.html', prediction_text='You have burned {} calories.'.format(prediction))

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     '''
#     For direct API calls trought request
#     '''
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])

#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)