import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Read dataset
df = pd.read_csv(".././dataset/sentences.csv")

# Load embeddings
embeddings = np.load(".././output/embeddings.npy")

# Compute cosine similarity matrix
similarity = cosine_similarity(embeddings)

# Save similarity matrix
pd.DataFrame(similarity, index=df["id"], columns=df["id"]).to_csv(".././output/cosine_similarity.csv")

print("Cosine Similarity Matrix Shape:", similarity.shape)
print("Saved to output/cosine_similarity.csv")