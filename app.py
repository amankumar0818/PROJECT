import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

st.title("Storyline Generator ✨")
st.write("Generate Storylines")

genre = st.text_input("Genre", "Fantasy")
characters = st.text_input("Characters (comma-separated)")
length = st.selectbox("Length", ["short", "medium", "long"])
tone = st.text_input("Tone", "Hopeful")
extras = st.text_area("Special elements (optional)")

if st.button("Generate Storyline"):

    if not API_KEY:
        st.error("GROQ_API_KEY missing in .env file")

    else:
        client = Groq(api_key=API_KEY)

        prompt = f"""
Write a {length} {genre} storyline.

Characters: {characters}
Tone: {tone}
Special elements: {extras}

Make the storyline creative, engaging and suitable for the selected length.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.subheader("Generated Storyline")
        st.write(response.choices[0].message.content)