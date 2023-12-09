from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load the saved model
model = pickle.load(open("best_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html", prediction_text='')

@app.route("/predict", methods=["POST"])
def predict():
    # Load input values from the form
    Model_Year = float(request.form["Model_Year"])
    Airbag = float(request.form["Airbag"])
    Air_Conditioning = float(request.form["Air_Conditioning"])
    Central_Locking = float(request.form["Central_Locking"])
    Alarm = float(request.form["Alarm"])
    Sunroof = float(request.form["Sunroof"])
    age = float(request.form["age"])

    # Prepare the input data for prediction
    data = {'Model_Year': [Model_Year], 'Airbag': [Airbag], 'Air_Conditioning': [Air_Conditioning],
            'Central_Locking': [Central_Locking], 'Alarm': [Alarm], 'Sunroof': [Sunroof], 'age': [age]}
    input_data = pd.DataFrame(data)

    # Make predictions using the loaded model
    prediction = model.predict(input_data)[0]

    # Format the prediction result
    prediction_text = f"The predicted selling price of the car is: {prediction:.2f}"

    # Print the prediction for debugging
    print("Prediction:", prediction)

    # Return the predicted price to the HTML page
    return render_template("index.html", prediction_text=prediction_text, predicted_price=prediction)

if __name__ == "__main__":
    app.run(debug=True)
