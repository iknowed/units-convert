# units-convert
repository for coding challenge

I've solved the conversion problem using a graph to represent conversion paths between all units.

Kelvin is the common unit, all other units convert to Kelvin and all units can be converted to from Kelvin.

This allows for extensibility.

The graph is traversed using dijkstra's algorithm and for each edge the source and target units are determined. Using 
python intropection, a pointer to the appropriate conversion method is acquired and used to make the call to convert.

I've reused the Node and Graph classes from a previous project.

The Convert class contains the logic of how to use Node/Graph to walk the topology.

Test of functionality is in the main method of convert.py:

$ python convert.py

Unittests are in the test\*.py files:

python -m unittest testConvert
python -m unittest testNode
python -m unittest testGraph

A much wider scope of testing could be implemented.
