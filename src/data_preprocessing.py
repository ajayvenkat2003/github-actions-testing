import sys,os
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import torch
from torch import nn
t = torch.randint(1,2,(2,2))
t.type_as(torch.float16)
t._grad