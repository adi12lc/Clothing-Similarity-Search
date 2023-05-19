from sentence_transformers import SentenceTransformer
from flask import Flask, request, render_template
import pandas as pd
from google.cloud import storage
from io import BytesIO
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)
app.config["HOST"] = "0.0.0.0"
app.config["PORT"] = 8080

# Initialize SentenceTransformer model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def download_blob(bucket_name, source_blob_name):
            """Downloads a blob from the bucket."""
            storage_client = storage.Client()
            bucket = storage_client.bucket(bucket_name)
            blob = bucket.blob(source_blob_name)
            return blob.download_as_bytes()

def read_csv_from_gcs(bucket_name, source_blob_name):
            csv_bytes = download_blob(bucket_name, source_blob_name)
            return pd.read_csv(BytesIO(csv_bytes))

# Read the CSV file from the google cloud bucket 
df = read_csv_from_gcs('cloth_project_data', 'Cloth_description_data.csv')

# Encode detail descriptions
df['embeddings'] = df['detail_description'].apply(lambda x: model.encode(x))

# Route for recommendation
@app.route('/', methods=['GET', 'POST'])
def recommend():
    # Initialize recommendation and link lists
    recommendations = [None] * 5
    links = [None] * 5
    user_description = "Description"
    index = []

    if request.method == 'POST':
        # Get user description from form
        user_description = request.form.get('description')

        # Encode user description
        user_embedding = model.encode(user_description)

        # Calculate similarity between user embedding and each detail description embedding
        df['similarity'] = cosine_similarity(np.vstack(df['embeddings'].values), [user_embedding])

        # Get the indexes of top 5 similar embeddings
        top_indexes = df['similarity'].argsort()[-5:][::-1]

        # Get the top 5 recommendations and their links
        recommendations = df.loc[top_indexes, 'title'].tolist()
        links = df.loc[top_indexes, 'URL'].tolist()

        # for indexing the items
        for i in range(1,6):
            index.append(i)

    return render_template('index.html', links=links, recommendations=zip(recommendations, links, index), description=user_description)


if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config["PORT"])


