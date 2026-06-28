import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Read dataset
df = pd.read_csv(".././dataset/sentences.csv")

# Load embeddings
embeddings = np.load(".././output/embeddings.npy")

# Perform t-SNE
tsne = TSNE(n_components = 2, random_state = 42, perplexity =5)

points = tsne.fit_transform(embeddings)

# Plot
plt.figure(figsize = (8, 6))

for i, sentence in enumerate(df["sentence"]):
    plt.scatter(points[i, 0], points[i, 1])
    plt.text(points[i, 0], points[i, 1], str(i + 1), fontsize = 9)

plt.title("Sentence Embedding Visualization using t-SNE")
plt.xlabel("t-SNE Dimension 1")
plt.ylabel("t-SNE Dimension 2")
plt.tight_layout()

plt.savefig(".././figures/tsne.png", dpi = 300)

plt.show()
