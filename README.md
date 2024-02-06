# Personalized-CoverLetter-Generator
## Project Overview
Welcome to an AI-Powered Personalized Cover Letter Generator! This project is an integrated application that harnesses the power of LangChain, OpenAI's GPT-3.5-turbo model, and Streamlit to generate personalized cover letters tailored to specific job opportunities. The system is designed to streamline the cover letter creation process by dynamically aligning extracted resume information with relevant details from job descriptions. The purpose of this project is to provide job seekers with an efficient and automated option for creating customized cover letters. 

## Technologies Used
1. LangChain - LangChain provides advanced natural language processing capabilities, enhancing the quality of language generation in the cover letters.

2. OpenAI GPT-3.5-turbo - GPT-3.5-turbo powers the intelligent generation of cover letter content, understanding and responding to prompts with human-like text.

3. SerpAPI - SerpAPI is integrated to streamline the cover letter personalization process by automatically extracting company job description URLs and key information.

4. Streamlit - Streamlit is used to build the user interface, providing a simple and interactive environment for users to generate and customize their cover letters.

5. PyCharm - PyCharm is the integrated development environment (IDE) used for coding and managing the project.

## Features
Integrated Application: Our project brings together various technologies, including LangChain, OpenAI’s GPT-3.5-turbo, SerpAPI, and Streamlit, to provide a seamless and efficient user experience for generating personalized cover letters.

Dynamic Prompt Templates: We have engineered dynamic prompt templates that intelligently align extracted resume information with relevant details from job descriptions. This ensures that your cover letters are tailored to the specific requirements of each job.

SerpAPI Integration: Leveraging SerpAPI, we have streamlined the cover letter personalization process by automatically extracting company job description URLs and key information. This integration enhances the accuracy and relevance of the generated cover letters.

## Getting Started

To use the AI-Powered Personalized Cover Letter Generator, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/amruthak03/Personalized-CoverLetter-Generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Personalized-CoverLetter-Generator
    ```

3. Open the `website_url_fetcher.py` file and replace the placeholder 'YOUR_API_KEY' with your actual API key wherever it is used:

    ```python
    # website_url_fetcher.py

    # Replace 'YOUR_API_KEY' with your actual API key
    serpapi_api_key = 'YOUR_API_KEY'
    openai_api_key = 'YOUR_API_KEY'
    ```

   Repeat this process for any other Python files in the project where 'YOUR_API_KEY' is used.

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the application:

    ```bash
    streamlit run streamlit_app.py
    ```

6. Access the application in your web browser at [http://localhost:8501](http://localhost:8501)
<img width="361" alt="image" src="https://github.com/amruthak03/Personalized-CoverLetter-Generator/assets/110037114/55b5f1f7-906b-44bd-a768-aa418f0ca04b">

The application looks like this

## Usage
1. Upload your resume and provide any additional information required.
2. Enter the company name and job title.
3. Click the "Generate Cover Letter" button.
5. Download the personalized cover letter.
6. Review and customize the generated cover letter as needed.

