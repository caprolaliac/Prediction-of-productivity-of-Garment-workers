from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('best_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        smv = float(request.form['smv'])
        wip = int(request.form['wip'])
        overtime = int(request.form['overtime'])
        quarter = request.form['quarter']
        day = request.form['day']

        user_data = pd.DataFrame({
            'smv': [smv],
            'wip': [wip],
            'over_time': [overtime],
            'quarter': [quarter],
            'day': [day]
        })

        user_data_encoded = pd.get_dummies(user_data, columns=['quarter', 'day'])

        X_columns = model.estimators_[0].feature_importances_
        X = user_data_encoded.reindex(columns=X_columns, fill_value=0)

        prediction = model.predict(X)[0]

        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
