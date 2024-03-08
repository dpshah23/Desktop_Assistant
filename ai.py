import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import speak as sp



genai.configure(api_key='AIzaSyCCajhYEs4x4ZvcobyCwvUCc9AAcUqb3Mw')
model = genai.GenerativeModel('gemini-pro')
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def ans(text):
    sp.speak("Waiting for Result")
    response = model.generate_content(text)
    response1=to_markdown(response.text)
    print(response1)


ans("PAN in computer Network")


