# Documentation for the Flask-based Recommendation System

## Introduction

This documentation explains a Flask-based recommendation system application that utilizes the Sentence Transformers model and Google's BigQuery for fetching data. The application receives a user's text description and returns the most similar items from a database. 

## Step-by-step Process

1. **Import Required Libraries:** The necessary libraries for the application are imported. These include Flask for the web application, SentenceTransformer for transforming sentences into embeddings, BigQuery for fetching data, and cosine_similarity for similarity measurement.

2. **Initialize the Flask Application:** A new Flask application instance is created and configured with the host and port number.

3. **Load the Sentence Transformer Model:** The SentenceTransformer model is loaded for use in transforming sentences into embeddings.

4. **Initialize Embedding Storage Class:** This class is responsible for fetching data from BigQuery, calculating embeddings for each data entry, and storing these embeddings for later use. The class also includes a method to find similar items based on a given description.

5. **Create an Instance of Embedding Storage:** An instance of the Embedding Storage class is created, and it fetches the data from BigQuery, calculates, and stores the embeddings.

6. **Define a Route for the Recommendation System:** The `recommend()` function is defined as the main route of the application. This function is responsible for handling GET and POST requests, receiving the user's description, calling the get_similar_items method of the EmbeddingStorage instance, and rendering the results on a webpage.

7. **Run the Application:** Finally, the Flask application is started and set to listen for incoming connections on the specified host and port.

## Detailed Explanation of the Steps

- **Step 1:** Importing the necessary libraries for creating the web application, handling the data, generating sentence embeddings, and comparing embeddings for similarity.

- **Step 2:** Initializing a Flask application that will serve as the interface between the user and the recommendation system.

- **Step 3:** Loading the SentenceTransformer model that will be used to generate embeddings of sentences. The model name "sentence-transformers/all-MiniLM-L6-v2" is a pre-trained model and can be replaced with any other suitable SentenceTransformer model.

- **Step 4:** The EmbeddingStorage class has several responsibilities: 
    - In the constructor (`__init__`), it initializes the BigQuery client, runs the given SQL query, and computes embeddings for the fetched data.
    - The `get_bigquery_data()` method executes the provided SQL query using the BigQuery client and stores the result in a pandas DataFrame.
    - The `update_embeddings()` method fetches the latest data and computes their embeddings using the SentenceTransformer model.
    - The `get_similar_items()` method computes the cosine similarity between a given description and the stored embeddings, finds the most similar items, and returns their titles and URLs.

- **Step 5:** An instance of the EmbeddingStorage class is created, using a SQL query to fetch the data from BigQuery and the loaded SentenceTransformer model to compute embeddings.

- **Step 6:** The `recommend()` function is defined as a Flask route that responds to both GET and POST requests. If the request method is POST, it gets the user's description from the request, uses the EmbeddingStorage instance to find the most similar items, and prepares them for rendering. Then it renders a webpage using a template called "index.html", passing the recommended items and their URLs to the template.

- **Step 7:** The Flask application is run, starting the server and listening for incoming connections on the configured host and port.

Please ensure that you have all the necessary libraries installed, and the BigQuery data is accessible from your environment. You also need to have a

 template named 'index.html' in a templates folder in your project directory. This template should be designed to properly display the information passed to it from the `recommend()` function.