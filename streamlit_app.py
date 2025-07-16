import streamlit as st
import pandas as pd
import altair as alt

df = pd.read_csv("assets/listings(1).csv.gz", compression='gzip')
df = df.dropna(subset=['price', 'review_scores_rating'])
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

# Sidebar filters
neighborhood = st.selectbox("Select Neighborhood", df['neighbourhood_cleansed'].unique())
min_price = st.slider("Minimum Price", 0, 1000, 100)

filtered_df = df[(df['neighbourhood_cleansed'] == neighborhood) & (df['price'] >= min_price)]

# Altair Chart 1: Price vs. Number of Reviews
scatter = alt.Chart(filtered_df).mark_circle(size=60, opacity=0.5).encode(
    x='number_of_reviews:Q',
    y='price:Q',
    tooltip=['name', 'price', 'number_of_reviews']
).properties(title="Price vs Number of Reviews")

# Altair Chart 2: Histogram of Review Scores
hist = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('review_scores_rating:Q', bin=True),
    y='count()'
).properties(title="Distribution of Review Scores")

# Altair Chart 3: Average Price by Room Type
bar = alt.Chart(filtered_df).mark_bar().encode(
    x='room_type:N',
    y='mean(price):Q',
    color='room_type:N'
).properties(title="Average Price by Room Type")

st.altair_chart(scatter, use_container_width=True)
st.altair_chart(hist, use_container_width=True)
st.altair_chart(bar, use_container_width=True)