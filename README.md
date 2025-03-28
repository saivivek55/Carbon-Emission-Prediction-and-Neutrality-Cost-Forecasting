# 🌍 Carbon Emission Prediction & Neutrality Cost Forecasting

## 🔎 Project Overview
This project focuses on forecasting carbon emissions and estimating the cost of achieving carbon neutrality for top polluting countries. Leveraging a CRISP-DM methodology, the analysis uses time-series modeling to support sustainable policy decisions and emission management strategies.

### 📊 Datasets Used
- **World Data:** Contains global carbon emission indicators collected from the World Bank, covering 245 countries and 80+ environmental features.
- **USA Data:** Includes national-level carbon emission metrics sourced from the U.S. Energy Information Administration (EIA), provided as multiple time-series records.

## ⚙️ Modeling Approach
We explored and evaluated multiple machine learning models:
- **Hybrid CNN-IBFA**
- **Support Vector Regression (SVR)**
- **Long Short-Term Memory (LSTM)**

Based on model performance, the **LSTM model**- achieving an MSE of 0.0038 and R² of 0.8892, was selected for final forecasting due to its effectiveness in capturing long-term temporal dependencies in emission trends.

### 🧪 Evaluation Metrics
Each model was assessed using:
- **MSE** (Mean Squared Error)  
- **MAE** (Mean Absolute Error)  
- **R²** (R-squared)

The LSTM model achieved the best overall results, making it ideal for predicting both emissions and neutrality cost scenarios.

## 📈 Key Features
- Time-series forecasting of carbon emissions using LSTM  
- Emission trend analysis across key global and national datasets  
- Carbon neutrality cost prediction for top polluting countries  
- **Web-based dashboard** to visualize emission forecasts and policy-level cost implications

## 🧰 Tech Stack
- **Python**  
- **LSTM, SVR, Hybrid CNN-IBFA**  
- **NumPy, Pandas, Matplotlib, Seaborn**  
- **Jupyter Notebook**  

## 🚀 How to Run
1. **Clone the Repository**
   ```bash
   git clone https://github.com/saivivek55/Carbon-Emission-Prediction-and-Neutrality-Cost-Forecasting.git
   cd Carbon-Emission-Prediction-and-Neutrality-Cost-Forecasting
2. **Install Dependencies**
3. **Execute the python files**

## 🔍 Key Insights                                                                                                                                                                                                                        
- Datasets: Global and national datasets revealed region-specific emission behavior trends.                                                                                                             
- Robust Forecasting: Achieved low MSE with a high R² value using the LSTM model.                                                                                                
- Actionable Outcomes: Provided precise carbon neutrality cost forecasts, guiding policy formulation and sustainable planning.                                                                                                                                              

## 📄 License                                                                                                                                                                                                                                                                                                                                   
This project is licensed under the Apache 2.0 License.
