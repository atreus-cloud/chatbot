from sentence_transformers import SentenceTransformer as st
import faiss as fs
import numpy as np

class embeddings:
    def __init__(self):
        self.model = st("all-MiniLM-L6-v2")
        self.index = None #temporariliy 
        self.docs = []
        self.embed = []

    def buildIndex(self, docs):
        self.docs = docs
        self.embed = self.model.encode(docs, convert_to_numpy = True)
        self.dimension = self.embed.shape[1]
        self.index = fs.IndexFlatL2(dim)
        self.index.add(self.embed)
    
    def chatbotQuery(self, q):
        q_embed = self.model.encode([q], convert_to_numpy=True)
        q_vec = q_embed[0]
        dist_vec, ind = self.index.search(q_vec, 4) #top 4 docs
        for i in ind[0]:
            results = self.docs[i]
        return results


