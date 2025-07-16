import streamlit as st
import altair as alt
from vega_datasets import data


# Load dataset
cars = data.cars()


# Scatter plot using Altair
scatter = alt.Chart(cars).mark_circle(size=60).encode(
    x="Horsepower",
    y="Miles_per_Gallon",
    color="Origin",
    tooltip=["Horsepower", "Miles_per_Gallon", "Origin"]
).interactive()


# Streamlit app
st.title("Altair Scatterplot in Streamlit")
st.write("This scatterplot shows the relationship between Horsepower and MPG in cars.")
st.altair_chart(scatter, use_container_width=True)