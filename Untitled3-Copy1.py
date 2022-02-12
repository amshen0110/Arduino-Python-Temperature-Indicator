#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pyfirmata as pf
from jupyterplot import ProgressPlot
import time


# In[6]:


board = pf.Arduino("COM4")
it = pf.util.Iterator(board)
it.start()


# In[7]:


a0 = board.get_pin('a:0:i')


# In[10]:


voltage = a0.read()*5
current = (voltage)/1000
resistence = (3.3-voltage)/current
print(voltage)
print(resistence)
temp = ((resistence/3.902)-(1/0.003902))
print(temp)


# In[ ]:





# In[ ]:




