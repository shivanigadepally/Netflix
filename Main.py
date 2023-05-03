import streamlit as st
import pandas as pd
import altair as alt
import io
import os
from PIL import Image
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud


st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; font-family:Sans-serif; font-size: 50px; color: red;'>Netflix Data Analysis</h1>", unsafe_allow_html=True)
st.write('')
st.write("Netflix is a streaming service that offers a wide variety of TV shows, movies, web series, documentaries,and more. Today, Netflix has over <span style='color:yellow'>209 million subscribers</span> in more than <span style='color:yellow'>190 countries.</span> It produces its own original content. Netflix offers a variety of subscription plans, with different pricing and features. Subscribers can access Netflix on their TVs, computers, mobile devices, and gaming consoles. The platform uses algorithms to recommend content to users based on their viewing history, and allows users to create multiple profiles within a single account.", unsafe_allow_html=True)
st.write('')
images_dir = os.path.join(os.getcwd(), 'data')

# Load a sequence of images
images = []
for i in range(2):
    image_path = os.path.join(images_dir, f"image_{i}.png")
    image = Image.open(image_path)
    images.append(image)

# Create a GIF animation from the images
with io.BytesIO() as output:
    images[0].save(output, format="png", save_all=True, append_images=images[1:], duration=100, loop=0)
    data = output.getvalue()


# Display the GIF animation
st.image(data, use_column_width=True  )

st.write('')
#st.subheader ('About the Dataset')

st.markdown("<h2 style='color: red;'>About the Dataset</h2>", unsafe_allow_html=True)
st.write('The data shows the pricing, subscriptions and revenue of the source. Over the last few years the library size and monthlycosts of the Netflix subscriptionsaround the worldoften finding a huge disparity. Netflix slashed its prices across more than 100 countries, especially for basic plans in African and Asian countries. This coincided with its announcement that it was starting to crack down on password sharing outside of one household, with the likes of Canada, New Zealand, Spain, and Portugal being the first to see these changes.')
st.markdown('')