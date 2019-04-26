# Multiplex Diseasome Communities

Online supplementary material for [Halu, A., De Domenico, M., Arenas, A. and Sharma, A., The multiplex network of human diseases. npj Systems Biology and Applications, 5 (1) pp: 15 (2019)](https://www.nature.com/articles/s41540-019-0092-5)

## Interactive mode -- Bokeh server:
To explore Multiplex Disease Communities in interactive mode where disease communities can be selected through a dropdown menu, follow the steps below.

- Download [Similarity_df_dict_top30_hierarchical.npy](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/Similarity_df_dict_top30_hierarchical.npy)

- In [MultiplexDiseaseCommunities.py](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/MultiplexDiseaseCommunities.py) replace `path` with the directory the above file was saved

- (1) To run the Bokeh server, navigate to the directory that has the the Python script [MultiplexDiseaseCommunities.py](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/MultiplexDiseaseCommunities.py) and type `bokeh serve --show MultiplexDiseaseCommunities.py` or (2) to run the interactive Bokeh app in a Jupyter notebook, open [MultiplexDiseasomeCommunities.ipynb](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/MultiplexDiseasomeCommunities.ipynb) directly in Jupyter and execute all the cells.


## Interactive mode -- nbviewer:
Alternatively, to visualize all Multiplex Disease Communities in interactive mode, [nbviewer](https://nbviewer.jupyter.org/) can be used to render the Jupyter notebook [MultiplexDiseasomeCommunities_all.ipynb](https://github.com/r-duh/MultiplexDiseasomeCommunities/blob/master/MultiplexDiseasomeCommunities_all.ipynb) via the url:

https://nbviewer.jupyter.org/github/r-duh/MultiplexDiseasomeCommunities/blob/master/MultiplexDiseasomeCommunities_all.ipynb

(scroll down to see the heatmaps for each disease community)

## Usage
Hover mouse over the heatmaps to view the respective molecular (GO:BP and gene overlap) or phenotypic (RR comorbidity or MimMiner) similarity measure between any two diseases within a multiplex disease community. Heatmaps can be panned and zoomed in to using the Bokeh tools on the upper right corner of each community window.

