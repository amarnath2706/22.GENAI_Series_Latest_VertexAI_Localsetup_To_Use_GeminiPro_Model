import vertexai
import streamlit as st
import os

from vertexai.preview.generative_models import (
    GenerationConfig,
    GenerativeModel
    )

from dotenv import load_dotenv

load_dotenv()

project_id = os.getenv("project_id")
project_region = os.getenv("region")

#Authenticate with vertexai
vertexai.init(project=project_id, location=project_region)

#load the model
model = GenerativeModel("gemini-1.0-pro")