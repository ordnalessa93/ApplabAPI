import numpy as np
try:
  from . import DataHandler
except ImportError:
  from utils import DataHandler
from DataHandler import ParameterExtractor, DataHandler

handler = DataHandler()
params = []
date_id=None
for user_id in handler.user_ids:
    if date_id is None:
        answers = handler.corrects[np.where(handler.user_ids == user_id)]
    else:
        answers = handler.corrects[np.where((handler.user_ids == user_id) &
                                         (handler.dates == date_id))]
    same = list(np.ones(len(answers)))
    try:
        same[0] = 0
        parameter = ParameterExtractor().smart_ssr(answers, same, 1000, 5)
        params.append([user_id, *parameter])
    except IndexError:
        params.append([user_id, None, None, None, None])
np.savetxt("../../data/parameters.csv", params)


