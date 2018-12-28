import sys 
import os
import numpy as np
import pandas as pd

from bokeh.plotting import figure, gridplot, show, output_file, output_notebook, ColumnDataSource, curdoc
from bokeh.models.widgets import Paragraph, Div
from bokeh.layouts import row, widgetbox, column
from bokeh.models import CustomJS, Select, HoverTool
from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application

output_file('multiplex_clusters.html')
    
def update_df(clu, bokeh_df_dict):

	return bokeh_df_dict[clu]

def callback(attr, old, new):

	new_bokeh_df = update_df(select.value, bokeh_df_dict) # get drowpdown menu value and put instead of "n_clu"
	source1.data = ColumnDataSource(new_bokeh_df['comorbidity_df']).data
	source2.data = ColumnDataSource(new_bokeh_df['mimminer_df']).data  
	source3.data = ColumnDataSource(new_bokeh_df['GOBP_df']).data  
	source4.data = ColumnDataSource(new_bokeh_df['geneoverlap_df']).data  
	
	new_len_labels1 = int(len(new_bokeh_df['comorbidity_df'])**0.5)  
	p1.x_range.factors = list(source1.data['yname'][0:new_len_labels1])
	p1.y_range.factors = list(source1.data['yname'][0:new_len_labels1])
	new_len_labels2 = int(len(new_bokeh_df['mimminer_df'])**0.5)  
	p2.x_range.factors = list(source2.data['yname'][0:new_len_labels2])
	p2.y_range.factors = list(source2.data['yname'][0:new_len_labels2])
	new_len_labels3 = int(len(new_bokeh_df['GOBP_df'])**0.5)  
	p3.x_range.factors = list(source3.data['yname'][0:new_len_labels3])
	p3.y_range.factors = list(source3.data['yname'][0:new_len_labels3])
	new_len_labels4 = int(len(new_bokeh_df['geneoverlap_df'])**0.5)  
	p4.x_range.factors = list(source4.data['yname'][0:new_len_labels4])
	p4.y_range.factors = list(source4.data['yname'][0:new_len_labels4])    
	text.text = '</br>'.join(sorted(list(set(source1.data['yname']) | set(source2.data['yname']) |
										set(source3.data['yname']) | set(source4.data['yname'])), 
									key=lambda s: s.lower())).replace('_', ' ')
  
#----------------------------------------------------------------------------------------------------------------

#bokeh_df_dict = {}
#for n_clu in np.arange(0, 10):
#    bokeh_df_dict['Community %s' % n_clu] = calculate_bokeh_similarity_df_hierarchical(n_clu)        
	
bokeh_df_dict = np.load('/Users/ardahalu/Desktop/Similarity_df_dict_top30_hierarchical.npy').item()   
init_comm = 'Community 8'

#----------------------------------------------------------------------------------------------------------------

source1 = ColumnDataSource(bokeh_df_dict[init_comm]['comorbidity_df'])
len_labels1 = int(len(bokeh_df_dict[init_comm]['comorbidity_df'])**0.5)
labels1 = list(source1.data['yname'][0:len_labels1])    

p1 = figure(title="RR Comorbidity", x_axis_location="above", tools="hover,save,wheel_zoom,pan",
		   x_range=labels1, y_range=labels1)

p1.grid.grid_line_color = None
p1.axis.axis_line_color = None
p1.axis.major_tick_line_color = None
p1.axis.major_label_text_font_size = "6pt"
p1.axis.major_label_standoff = 0
p1.xaxis.major_label_orientation = np.pi/2

p1.rect('xname', 'yname', 0.9, 0.9, source=source1, color='colors', alpha='comorbidity_alpha', line_color=None,
	   hover_line_color='black', hover_color='colors')

hover = HoverTool(tooltips=[("Disease 1", "@xname"), ("Disease 2", "@yname"), 
							("Comorbidity (log RR)", "@comorbidity")])
p1.add_tools(hover)
#----------------------------------------------------------------------------------------------------------------    

source2 = ColumnDataSource(bokeh_df_dict[init_comm]['mimminer_df'])
len_labels2 = int(len(bokeh_df_dict[init_comm]['mimminer_df'])**0.5)
labels2 = list(source2.data['yname'][0:len_labels2])   
	
p2 = figure(title="MimMiner", x_axis_location="above", tools="hover,save,wheel_zoom,pan",
		   x_range=labels2, y_range=labels2)

p2.grid.grid_line_color = None
p2.axis.axis_line_color = None
p2.axis.major_tick_line_color = None
p2.axis.major_label_text_font_size = "6pt"
p2.axis.major_label_standoff = 0
p2.xaxis.major_label_orientation = np.pi/2

p2.rect('xname', 'yname', 0.9, 0.9, source=source2, color='colors', alpha='mimminer_alpha', line_color=None,
	   hover_line_color='black', hover_color='colors')

hover = HoverTool(tooltips=[("Disease 1", "@xname"), ("Disease 2", "@yname"), 
							("MiMMiner", "@mimminer")])
p2.add_tools(hover) 
#----------------------------------------------------------------------------------------------------------------     

source3 = ColumnDataSource(bokeh_df_dict[init_comm]['GOBP_df'])
len_labels3 = int(len(bokeh_df_dict[init_comm]['GOBP_df'])**0.5)
labels3 = list(source3.data['yname'][0:len_labels3])   

p3 = figure(title="GO:BP", x_axis_location="above", tools="hover,save,wheel_zoom,pan",
		   x_range=labels3, y_range=labels3)

p3.grid.grid_line_color = None
p3.axis.axis_line_color = None
p3.axis.major_tick_line_color = None
p3.axis.major_label_text_font_size = "6pt"
p3.axis.major_label_standoff = 0
p3.xaxis.major_label_orientation = np.pi/2

p3.rect('xname', 'yname', 0.9, 0.9, source=source3, color='colors', alpha='GOBP_alpha', line_color=None,
	   hover_line_color='black', hover_color='colors')

hover = HoverTool(tooltips=[("Disease 1", "@xname"), ("Disease 2", "@yname"), 
							("GO:BP Similarity (GS2)", "@GOBP")])
p3.add_tools(hover)
#----------------------------------------------------------------------------------------------------------------

source4 = ColumnDataSource(bokeh_df_dict[init_comm]['geneoverlap_df'])
len_labels4 = int(len(bokeh_df_dict[init_comm]['geneoverlap_df'])**0.5)
labels4 = list(source4.data['yname'][0:len_labels4])   

p4 = figure(title="Gene overlap", x_axis_location="above", tools="hover,save,wheel_zoom,pan",
		   x_range=labels4, y_range=labels4)

p4.grid.grid_line_color = None
p4.axis.axis_line_color = None
p4.axis.major_tick_line_color = None
p4.axis.major_label_text_font_size = "6pt"
p4.axis.major_label_standoff = 0
p4.xaxis.major_label_orientation = np.pi/2

p4.rect('xname', 'yname', 0.9, 0.9, source=source4, color='colors', alpha='geneoverlap_alpha', line_color=None,
	   hover_line_color='black', hover_color='colors')

hover = HoverTool(tooltips=[("Disease 1", "@xname"), ("Disease 2", "@yname"), 
							("Gene Overlap (Jaccard)", "@geneoverlap")])
p4.add_tools(hover)
#-----------------------------------------------------------------------------------------------------------------


p = gridplot([[p3, p1], [p4, p2]], sizing_mode='fixed', plot_width=400, plot_height=400)

select = Select(title="Select a multiplex disease community:", value=init_comm, 
				options=sorted(bokeh_df_dict.keys()))
select.on_change('value', callback)


div = Div(text='<b>List of diseases:</b>', width=200, height=10)
text = Div(text='</br>'.join(sorted(list(set(source1.data['yname']) | set(source2.data['yname']) |
										set(source3.data['yname']) | set(source4.data['yname'])), 
									key=lambda s: s.lower())).replace('_', ' '),
									width=250, height=400)  
   
layout = row(column(widgetbox(select), div, text), p)
curdoc().add_root(layout)
