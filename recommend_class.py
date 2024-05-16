from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import ast

class movie_recommendation:
    def __init__(self):
        
        self.movies_csv=pd.read_csv('movies.csv',encoding='latin1')
        self.credits_csv=pd.read_csv('credits.csv',encoding='latin1')
        self.merge_dataset = self.movies_csv.merge(self.credits_csv, on="title")
        self.merge_dataset = self.merge_dataset[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
        self.merge_dataset.dropna(inplace=True)
        self.merge_dataset['cast'] = self.merge_dataset['cast'].apply(self.get_cast_names)
        self.merge_dataset['crew'] = self.merge_dataset['crew'].apply(self.get_crew_directors)
        self.merge_dataset['overview'] = self.merge_dataset['overview'].apply(lambda x: x.split())
        self.merge_dataset['cast'] = self.merge_dataset['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
        self.merge_dataset['crew'] = self.merge_dataset['crew'].apply(lambda x: [i.replace(" ", "") for i in x])
        self.merge_dataset['genres'] = self.merge_dataset['genres'].apply(self.convert)
        self.merge_dataset['keywords'] = self.merge_dataset['keywords'].apply(self.convert)
        self.merge_dataset['keywords'] = self.merge_dataset['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
        self.merge_dataset['genres'] = self.merge_dataset['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
        
        self.merge_dataset['all_infos'] = self.merge_dataset['overview']+self.merge_dataset['genres']+self.merge_dataset['keywords']+self.merge_dataset['cast']+self.merge_dataset['crew']

        self.new_dataset=self.merge_dataset[["movie_id", "title", "all_infos"]]
        
        self.cv = CountVectorizer(max_features=5000, stop_words="english")
        
        self.new_dataset['all_infos'] = self.new_dataset['all_infos'].apply(lambda x:' '.join(x))
        
        self.vectors = self.cv.fit_transform(self.new_dataset['all_infos']).toarray()

        self.porter = PorterStemmer()
        
        self.new_dataset['all_infos'] = self.new_dataset['all_infos'].apply(self.clean_sentence)
        
        self.similarity = cosine_similarity(self.vectors)
    
    
    def recommend(self, movie):
        movies_list = []
        movie_index = self.new_dataset[self.new_dataset['title']==movie].index[0]
        distances = self.similarity[movie_index]
        movie_sort = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
        for i in movie_sort:
            movies_list.append(self.new_dataset.iloc[i[0]].title)
        return movies_list
        
        
    def clean_sentence(self, text):
        y = []
        for i in text.split():
            y.append(self.porter.stem(i))
        return " ".join(y)


    def convert(self, obj):
        l = []
        for row in ast.literal_eval(obj):
            l.append(row['name'])
        return l


    def get_cast_names(self, obj):
        l = []
        for row in ast.literal_eval(obj):
            for i in range(5):
                l.append(row['name'])
        return l


    def get_crew_directors(self, obj):
        l = []
        for row in ast.literal_eval(obj):
            if row["job"] == "Director":
                l.append(row['name'])
        return l
    
    
# make_obj = movie_recommendation()
# print(make_obj.recommend("Avatar"))