
# coding: utf-8

# In[169]:


get_ipython().system(u'pip install docplex --upgrade')
import sys
import docplex.mp


# In[170]:

#put your API url and key here
url = None
key = None



# In[171]:


# first import the Model class from docplex.mp
from docplex.mp.model import Model

# create one model instance, with a name
m = Model(name='microservices-throughput')


# In[172]:


# by default, all variables in Docplex have a lower bound of 0 and infinite upper bound
service1 = m.integer_var(name='service1')
service2 = m.integer_var(name='service2')
service3 = m.integer_var(name='service3')
service4 = m.integer_var(name='service4')


# In[173]:



m.add_constraint(service1 >= 0)
m.add_constraint(service2 >= 0)
m.add_constraint(service3 >= 0)
m.add_constraint(service4 >= 0)
m.add_constraint(service3 >= 400)


# constraint #3: throughput-max
ct_maintenance = m.add_constraint (2*service1 + 3*service2 + 4*service3 + 5*service4 <= 5000)
ct_throughput = m.add_constraint (3*service1 + 4*service2 + 5*service3 + 5*service4 <= 6000)
ct_total = m.add_constraint(service1 + service2 + service3 + service4 == 1500)




# In[174]:




m.minimize(17*service1 + 12*service2 + 8*service3 + 7*service4)


# In[175]:


s = m.solve(url=url, key=key)
m.print_solution()
