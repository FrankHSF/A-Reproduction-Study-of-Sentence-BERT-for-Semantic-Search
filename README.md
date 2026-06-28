# A Reproduction Study of Sentence-BERT for Semantic Search



A reproduction study of **Sentence-BERT** for semantic search using the **sentence-transformers** library.



This repository accompanies the IEEE-style report:



**A Reproduction Study of Sentence-BERT for Semantic Search**





## Project Overview



This project reproduces the semantic search workflow proposed in the original Sentence-BERT paper.



The reproduction includes:

* Sentence embedding generation
* Cosine Similarity computation
* t-SNE visualization
* Experimental analysis



The implementation is based entirely on publicly available software libraries without modifying the original Sentence-BERT architecture.





## Experimental Environment



|Item|Specification|
|-|-|
|Operating System|Windows 11 Pro 25H2|
|Python|3.14.2|
|IDE|Visual Studio Code|
|CPU|Intel Core Ultra 9 285H|
|RAM|32 GB|
|Framework|PyTorch|
|Library|sentence-transformers|
|Similarity|Cosine Similarity|
|Visualization|t-SNE|





## Folder Structure



SentenceBERT_Reproduction/
dataset/
figures/
model/
output/
source/
requirements.txt
README.md
main.py





## Installation



git clone <https://github.com/FrankHSF/A-Reproduction-Study-of-Sentence-BERT-for-Semantic-Search>



cd SentenceBERT\_Reproduction



python -m venv .venv



.venv\\Scripts\\activate



pip install -r requirements.txt





## Run



Execute the complete experiment:



python main.py



or run each module separately:



python source/01\_generate\_embeddings.py



python source/02\_cosine\_similarity.py



python source/03\_tsne\_visualization.py





## Output



The experiment generates:



output/
embeddings.npy
cosine\_similarity.csv



figures/
tsne.png





## Paper



IEEE Report



**A Reproduction Study of Sentence-BERT for Semantic Search**





## References



# References

\[1] N. Reimers and I. Gurevych, "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks," in *Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)*, Hong Kong, China, Nov. 2019, pp. 3982 V3992.



\[2] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," in *Proceedings of NAACL-HLT 2019*, Minneapolis, MN, USA, Jun. 2019, pp. 4171 V4186.



\[3] T. Wolf *et al*., "Transformers: State-of-the-Art Natural Language Processing," in *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*, 2020, pp. 38 V45.



\[4] L. van der Maaten and G. Hinton, "Visualizing Data using t-SNE," *Journal of Machine Learning Research*, vol. 9, pp. 2579 V2605, Nov. 2008.



\[5] F. Pedregosa *et al*., "Scikit-learn: Machine Learning in Python," *Journal of Machine Learning Research*, vol. 12, pp. 2825 V2830, 2011.



\[6] A. Paszke *et al*., "PyTorch: An Imperative Style, High-Performance Deep Learning Library," in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 32, 2019.



\[7] T. Mikolov, K. Chen, G. Corrado, and J. Dean, "Efficient Estimation of Word Representations in Vector Space," in *Proceedings of the International Conference on Learning Representations (ICLR Workshop)*, 2013.



\[8] J. Pennington, R. Socher, and C. D. Manning, "GloVe: Global Vectors for Word Representation," in *Proceedings of EMNLP 2014*, Doha, Qatar, Oct. 2014, pp. 1532 V1543.



\[9] A. Singhal, "Modern Information Retrieval: A Brief Overview," *IEEE Data Engineering Bulletin*, vol. 24, no. 4, pp. 35 V43, Dec. 2001.



\[10] N. Reimers and I. Gurevych, *Sentence-Transformers: Multilingual Sentence, Paragraph, and Image Embeddings using BERT \& Co.*, Online Documentation. Available: https://www.sbert.net/. Accessed: Jun. 2026.





## License



MIT License

