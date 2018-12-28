# Multiplex Diseasome Communities

## Interactive mode:
To explore Multiplex Diseaes Communities in interactive mode where disease communities can be selected through a dropdown menu, follow the steps below.

- Download [Similarity_df_dict_top30_hierarchical.npy](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/Similarity_df_dict_top30_hierarchical.npy)

- In [MultiplexDiseaseCommunities.py](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/MultiplexDiseaseCommunities.py) replace `path` with the directory the above file was saved

- (1) To run the Bokeh server, navigate to the directory that has the the Python script [MultiplexDiseaseCommunities.py](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/MultiplexDiseaseCommunities.py) and type `bokeh serve --show MultiplexDiseaseCommunities.py` or (2) to run the interactive Bokeh app in a Jupyter notebook, open [MultiplexDiseasomeCommunities.ipynb](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/MultiplexDiseasomeCommunities.ipynb) directly in Jupyter and execute all the cells.


## Static mode:
To explore all Multiplex Disease Communities in static mode, [nbviewer](https://nbviewer.jupyter.org/) can be used to render the Jupyter notebook [MultiplexDiseasomeCommunities_static.ipynb](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/MultiplexDiseasomeCommunities_static.ipynb).

- The first step is the same as above -- download [Similarity_df_dict_top30_hierarchical.npy](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/Similarity_df_dict_top30_hierarchical.npy)

- Run [MultiplexDiseasomeCommunities_static.ipynb](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/MultiplexDiseasomeCommunities_static.ipynb) in [nbviewer](https://nbviewer.jupyter.org/) by via the url (https://nbviewer.jupyter.org/github/r-duh/MultiplexDiseasomeCommunities/blob/master/MultiplexDiseasomeCommunities_static.ipynb), making sure `path` points to the correct directory.
