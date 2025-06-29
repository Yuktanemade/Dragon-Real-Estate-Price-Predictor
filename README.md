🐉 Dragon Real Estate Price Predictor

A simple and interactive web application built using **Streamlit** to predict house prices based on 13 housing features. This project utilizes a trained machine learning model on the Boston Housing Dataset to predict modern real estate prices.

## 🚀 Features

- 🔢 Accepts 13 input features from the user
- 🧠 Uses a pre-trained model to make predictions
- 💸 Displays house price in INR and 💵 USD
- 🎨 Beautiful UI with background image and styled input fields
- 🎈 Balloons animation on successful prediction


## 📊 Input Features
   Attribute Information:

    1. CRIM      per capita crime rate by town
    2. ZN        proportion of residential land zoned for lots over 
                 25,000 sq.ft.
    3. INDUS     proportion of non-retail business acres per town
    4. CHAS      Charles River dummy variable (= 1 if tract bounds 
                 river; 0 otherwise)
    5. NOX       nitric oxides concentration (parts per 10 million)
    6. RM        average number of rooms per dwelling
    7. AGE       proportion of owner-occupied units built prior to 1940
    8. DIS       weighted distances to five Boston employment centres
    9. RAD       index of accessibility to radial highways
    10. TAX      full-value property-tax rate per $10,000
    11. PTRATIO  pupil-teacher ratio by town
    12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks 
                 by town
    13. LSTAT    % lower status of the population
    14. MEDV     Median value of owner-occupied homes in $1000's
 
## 🧠 Model Used

- The model is trained on the **Boston Housing Dataset**
- Saved as `Dragon.joblib` using `joblib`


📃 License
This project is licensed under the MIT License.


## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas, NumPy, Joblib**
- **Scikit-learn** (for model training)
- **HTML/CSS (inline)** for UI customization

  ## 🌐 Live App

> 🔗 [Click here to access the app](https://dragon-real-estate-price-predictor-8fjabvxuqj3qpjdqtaqxk9.streamlit.app/)  


## 🚀 How to Run Locally
```bash
# Clone the repository
git clone https://github.com/your-username/dragon-real-estate-price-predictor.git
cd dragon-real-estate-price-predictor

# Install dependencies
pip install streamlit pandas numpy scikit-learn joblib

# Run the app
streamlit run app.py






    
