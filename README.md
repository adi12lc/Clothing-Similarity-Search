# Clothing Similarity Search using NLP

This project aims to provide a clothing similarity search system using Natural Language Processing (NLP) techniques. It utilizes web scraping to gather clothing descriptions from the Amazon website, performs similarity modeling using Sentence Transformers, and deploying the application using Flask, Docker onto the Google Cloud Run.

## Motivation:
The motivation behind building this project is to provide users with an efficient and convenient way to search for clothing items based on their descriptions. Traditional search methods often rely on keyword matching, which may not capture the full context or nuances of a user's description. By utilizing NLP techniques, we can enhance the search capabilities and improve the user experience by providing more accurate and relevant recommendations.

## Building the Project:
This project was developed to leverage the power of NLP and web scraping to collect clothing descriptions, analyze their similarities, and recommend relevant clothing items to users. By employing sentence transformers, which are pretrained models capable of converting sentences into numerical representations, we can quantify the semantic similarity between the user's description and the dataset.

## Problem Solving:
The project addresses the problem of finding clothing items that closely match a user's description. By using NLP techniques, we can overcome the limitations of traditional keyword-based searches and provide more accurate recommendations. This system allows users to find clothing items that align with their desired style, characteristics, or features, even when they might not have a specific keyword in mind. By streamlining the search process and improving the precision of recommendations, this project aims to enhance the overall shopping experience for users.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [WebApp](#WebApp)

## Introduction

The Clothing Similarity Search project utilizes NLP techniques to enable users to search for clothing items based on their descriptions. The system is designed to recommend clothing items from a dataset scraped from the Amazon website that are most similar to the user's input.

The project follows the following steps:
1. Web scraping: Data is collected by scraping clothing descriptions from the Amazon website and stored in Google cloud stoarge buckets. The data is restricted to a limited range of clothing categories.
2. Similarity modeling: Sentence Transformers are used to convert clothing descriptions into numerical representations, enabling similarity comparisons.
3. Recommendation: Based on the user's input description, the system recommends clothing items with similar descriptions.
4. Deployment: The application is deployed on Google cloud run using Flask and Docker, making it accessible through the web.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Python (3.9 or higher)
- Flask
- Docker
- Google Cloud SDK (for deployment)

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/your-username/clothing-similarity-search.git
```

2. Change into the project directory:

```
cd clothing-similarity-search
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

## Usage

To use the clothing similarity search system locally, follow these steps:

1. Run the Flask application:

```
python flask_app.py
```

2. Open your web browser and navigate to `http://localhost:8080` to access the application.

3. Enter a description of the clothing item you are looking for in the input box and click the "Get recommendation" button.

4. The system will display a list of clothing items from the Amazon that are most similar to your input description.

## Deployment

To deploy the application on Google Cloud Run, follow these steps:

1. Create a project on Google Cloud Platform (GCP) if you haven't already done so.

2. Install and set up the Google Cloud SDK on your local machine.

3. Build the Docker image for the application:

```
docker build -t gcr.io/<your-gcp-project-id>/clothing-similarity-search .
```
   Replace `<your-gcp-project-id>` with your actual Google Cloud project ID.

4. After building the app, push it to Google Cloud:

```
gcloud auth configure-docker
docker push gcr.io/<your-gcp-project-id>/clothing-similarity-search
```

5. Deploy the application to Google Cloud Run:

```
gcloud run deploy --image gcr.io/your-project-id/clothing-similarity-search --platform managed
```

6. Follow the prompts to select a region and configure the deployment.

7. Once the deployment is complete, you will receive a URL where the application is accessible.

## WebApp

[https://ml-app-vt5twwhjza-uc.a.run.app/](https://clothing-similarity-search-vt5twwhjza-uc.a.run.app/)

Please utilize the provided link to access the web application that has been deployed on Google Cloud Platform (GCP) and assess its performance.

Note : The provided link may experience a delay in loading during its initial instance. Please be advised that the loading process might require some additional time to complete.
