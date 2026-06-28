import subprocess
import sys

steps = [
    "source/01_generate_embeddings.py",
    "source/02_cosine_similarity.py",
    "source/03_tsne_visualization.py"
]

print("=" * 60)
print("Sentence-BERT Reproduction Study")
print("=" * 60)

for step in steps:
    print(f"\nRunning: {step}")

    result = subprocess.run(
        [sys.executable, step]
    )

    if result.returncode != 0:
        print(f"\nFailed: {step}")
        exit(result.returncode)

print("\nExperiment completed successfully.")
print("Results are saved in:")
print("  output/")
print("  figures/")