import pickle
import random

def random_subject():
    with open('./data/subjects.pickle', 'rb') as f:
        subjects = pickle.load(f)
        return random.choice(subjects)

def random_predicate():
    with open('./data/predicates.pickle', 'rb') as f:
        predicates = pickle.load(f)
        return random.choice(predicates)
