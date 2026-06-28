from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

# Load pre-trained SBERT model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read dataset
df = pd.read_csv(".././dataset/sentences.csv")

# Generate sentence embeddings
embeddings = model.encode(df["sentence"].tolist(), convert_to_numpy = True)

print("Embedding Shape:", embeddings.shape)

# Save Embeddings
np.save(".././output/embeddings.npy", embeddings)

print("Embeddings saved to output/embeddings.npy")