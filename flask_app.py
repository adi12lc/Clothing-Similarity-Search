# Importing necessary libraries
from sentence_transformers import SentenceTransformer
from flask import Flask, request, render_template
from google.cloud import bigquery
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Initializing Flask app
app = Flask(__name__)
app.config["HOST"] = "0.0.0.0"
app.config["PORT"] = 8080

# Loading the SentenceTransformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Creating a class for managing and storing embeddings
class Embeddings:
    def __init__(self, query, model):
        # Initialize class with a SQL query and the sentence-transformer model
        self.query = query
        self.client = bigquery.Client()
        self.model = model
        self.update_embeddings()  # Update embeddings upon initialization

    def get_bigquery_data(self):
        # Run a BigQuery job, get the results, and convert to a DataFrame
        query_job = self.client.query(self.query)
        self.df = query_job.to_dataframe()

    def update_embeddings(self):
        # Update embeddings by fetching the latest data and computing their embeddings
        self.get_bigquery_data()
        descriptions = self.df['detail_description'].tolist()
        self.df['embeddings'] = list(self.model.encode(descriptions))

    def get_similar_items(self, description, n=5):
        # Get user's description
        user_embedding = self.model.encode([description])
        # Compute the cosine similarity between the provided description and stored embeddings
        self.df['similarity'] = cosine_similarity(np.vstack(self.df['embeddings'].values), user_embedding)
        top_indexes = self.df['similarity'].argsort()[-n:][::-1]  # Get the indices of top-n similar items
        recommendations = self.df.loc[top_indexes, 'title'].tolist()  # Get the titles of recommended items
        links = self.df.loc[top_indexes, 'URL'].tolist()  # Get the URLs of recommended items
        return recommendations, links

# SQL query to fetch data "newprojv1" - GCP project ID, "clothadi" - dataset name, "clothsearch" - table name.
query = "SELECT * FROM `newprojv1.clothadi.clothsearch`"
# Instantiate the Embedding class
storage = Embeddings(query, model)

# Define a route for the recommendation system
@app.route('/', methods=['GET', 'POST'])
def recommend():
    # Initialize variables
    recommendations = [None] * 5
    links = [None] * 5
    user_description = "Description"
    index = list(range(1, 6))

    if request.method == 'POST':
        # Get user's description from the form
        user_description = request.form.get('description')
        # Fetch recommended items and their links based on user's description
        recommendations, links = storage.get_similar_items(user_description)

    # Render the results on the webpage
    return render_template('index.html', links=links, recommendations=zip(recommendations, links, index), description=user_description)


# Run the Flask application
if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config["PORT"])


