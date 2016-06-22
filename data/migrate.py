import pickle

with open('subjects.txt', 'r') as subject_file:
    subjects = subject_file.readlines()
    subjects = [subject.replace('\n', '') for subject in subjects]

print subjects

with (open('subjects.pickle', 'wb')) as f:
    pickle.dump(subjects, f)

with open('predicates.txt', 'r') as predicate_file:
    predicates = predicate_file.readlines()
    predicates = [predicate.replace('\n', '') for predicate in predicates]

with (open('predicates.pickle', 'wb')) as f:
    pickle.dump(predicates, f)

print predicates
