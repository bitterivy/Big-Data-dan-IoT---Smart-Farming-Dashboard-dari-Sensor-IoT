import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Smart Agriculture Monitoring Dashboard")

# load dataset
df = pd.read_csv("data/raw/Smart Agriculture.csv")

st.subheader("Dataset Preview")
st.write(df.head())

# statistik
st.subheader("Statistik Data")
st.write(df.describe())

# temperature chart
st.subheader("Temperature Monitoring")
fig, ax = plt.subplots()
ax.plot(df['temp'].head(200))
ax.set_title("Temperature Trend")
st.pyplot(fig)

# humidity chart
st.subheader("Humidity Monitoring")
fig, ax = plt.subplots()
ax.plot(df['humidity'].head(200))
ax.set_title("Humidity Trend")
st.pyplot(fig)

# soil moisture chart
st.subheader("Soil Moisture Monitoring")
fig, ax = plt.subplots()
ax.plot(df['MOI'].head(200))
ax.set_title("Soil Moisture Trend")
st.pyplot(fig)

# correlation heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df[['MOI','temp','humidity','result']].corr(), annot=True, ax=ax)
st.pyplot(fig)
