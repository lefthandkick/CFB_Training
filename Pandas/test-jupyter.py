# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Pandas'))
	print(os.getcwd())
except:
	pass
#%%
import pandas


#%%
# df=pandas.read_csv("/Users/zaatas/AppDev/Python/Class_Projects/Pandas/data/noah-temps.csv")
df=pandas.read_csv("data/noah-temps.csv")
df


#%%
df=pandas.read_csv("data/store.csv")
df


#%%



