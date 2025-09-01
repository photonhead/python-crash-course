'''
8-17. Styling Functions: Choose any three programs you wrote for this chapter, 
and make sure they follow the styling guidelines described in this section.
'''
from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm

unprinted_designs = ['first floor', 'second floor', 'third floor', 'rooftop', 'garden', 'garage']
completed_models = []

pm(unprinted_designs[:], completed_models)
scm(completed_models)