import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np
from io import StringIO

# Streamlit Title
st.title("Sales Data Insights Tool 🚀")

# CSV Upload Section
uploaded_file = st.file_uploader("Upload your Sales Data CSV", type="csv")

if uploaded_file:
    # Load Data
    df = pd.read_csv(uploaded_file)
    st.write("### Data Loaded Successfully 🎉")
    st.dataframe(df)

    # Basic Sales Summary
    st.write("### Basic Sales Summary 📊")
    st.write(df.describe())

    # Total Sales by Category Visualization
    category_sales = df.groupby('Category')['Sales'].sum()
    fig, ax = plt.subplots()
    category_sales.plot(kind='bar', color=['skyblue', 'slateblue', 'steelblue'], ax=ax)
    plt.title("Total Sales by Category")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Percentage Growth Calculation
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values('Date', inplace=True)
    df['Sales Growth'] = df['Sales'].pct_change().fillna(0) * 100

    st.write("### Sales Growth (%) Over Time 📈")
    st.line_chart(df[['Date', 'Sales Growth']].set_index('Date'))

    # Prediction using Linear Regression
    st.write("### Sales Prediction (Linear Regression) 📡")

    # Prepare Data for Prediction
    df['Days'] = (df['Date'] - df['Date'].min()).dt.days
    X = df[['Days']]
    y = df['Sales']
    model = LinearRegression()
    model.fit(X, y)

    # Predict future sales
    future_days = np.array(range(df['Days'].max() + 1, df['Days'].max() + 10)).reshape(-1, 1)
    future_sales = model.predict(future_days)

    # Plot Prediction Results
    plt.figure(figsize=(10, 6))
    plt.plot(df['Days'], df['Sales'], label='Actual Sales')
    plt.plot(future_days, future_sales, label='Predicted Sales', linestyle='--', color='orange')
    plt.xlabel("Days from Start")
    plt.ylabel("Sales")
    plt.title("Sales Prediction for Next 10 Days")
    plt.legend()
    st.pyplot(plt)

    st.write("### Prediction Table 📋")
    prediction_df = pd.DataFrame({'Day': future_days.flatten(), 'Predicted Sales': future_sales})
    st.write(prediction_df)

else:
    st.info("Awaiting CSV Upload to Start the Analysis 📤")
