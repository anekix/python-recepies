'''
This is a small wrapper class using python-pptx & matplotlib.
It is used to generate graphs & charts which would be impossible to generate directly in python-pptx,
This exposes a cosistent api API which outputs either an <image object> or a <pptx slide object> depending upon requirement

** Graph() object has a factory method create() which is used to crate graphs of various types ex.. LineGraph & BarGraph

** Each graph-type class is a subclass of BaseGraph
'''

# grpahs.py

class BaseGraph:
	TYPE = None
  
	def generate(self):
		raise NotImplementedError()

	@classmethod
	def check_graph_type(cls,garph_type):
		return garph_type == cls.TYPE


class LineGraph(BaseGraph):
	TYPE = 'LINE'
	def __init__(self,data, x_axis, y_axis, x_label , y_label):
		# initialize variables
		pass

	def generate(self):
		# code to generate line graph...
		print ('generating LINE graph using Matplotlib')



class BarGraph(BaseGraph):
	TYPE = 'BAR'

	def __init__(self,data, x_axis, y_axis, x_label , y_label):
		# initialize variables
		pass


	def generate(self):
		# code to generate line graph ..
		print ('generating BAR graph using Matplotlib')



# core.py 

class Graph:
	GRAPHS_TYPES = [LineGraph, BarGraph]

	def __init__(self, graph_type, data , x_axis, y_axis, x_label, y_label):
		self.data = data
		self.x_axis = x_axis
		self.y_axis = y_axis
		self.x_label = x_label
		self.y_label = y_label

		self.graph_type = graph_type
		self.graph_engine = self.choose_graph_engine()


	def choose_graph_engine(self):
		for engine in self.GRAPHS_TYPES:
			if engine.check_graph_type(self.graph_type):
				return engine(self.data, self.x_axis, self.y_axis, self.x_label, self.y_label)

	def create(self):
		return self.graph_engine.generate()

	@property
	def pptx():
		# code to return  <pptx slide object>
		print ('graph as pptx slide object')

	@property
	def image():
		# code to return <image object>
		print ('graph as image object')




# client code
graph = Graph(
	graph_type='BAR',
	data=[1,2],
	x_axis=['a','b'],
	y_axis=['c','d'],
	x_label='country',
	y_label='population'
).create()


# image = graph.image
# pptx = graph.pptx
