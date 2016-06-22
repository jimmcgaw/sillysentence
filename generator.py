import pickle
import random
import os

def random_subject():
    filepath = os.path.join(os.path.dirname(__file__), 'data/subjects.pickle')
    with open(filepath, 'rb') as f:
        subjects = pickle.load(f)
        return random.choice(subjects)

def random_predicate():
    filepath = os.path.join(os.path.dirname(__file__), 'data/predicates.pickle')
    with open(filepath, 'rb') as f:
        predicates = pickle.load(f)
        return random.choice(predicates)
