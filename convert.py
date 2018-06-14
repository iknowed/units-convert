from graph import Graph

"""
    Module Docstring:
        this module is called convert
"""
class Convert(object):
    '''
        class convert
    '''
    def __init__(self):
        self.graph_dict= {}
        # set up conversion graph, all units lead to Kelvin, Kelvin leads to all units
        self.graph_dict['Kelvin'] = ['Celsius','Fahrenheit','Rankine']
        self.graph_dict['Celsius'] = ['Kelvin']
        self.graph_dict['Fahrenheit'] = ['Kelvin']
        self.graph_dict['Rankine'] = ['Kelvin']

        self.graph = Graph()

        # slurp in graph from dict to objects
        self.graph.graph_from_dict(self.graph_dict)

    def path(self, source, target):
        '''
            method path finds the conversion topology
        '''

        # run shortest path
        path = self.graph.dijkstra(source, target)
        return path

    # conversion routines

    def Celsius_to_Kelvin(self,degC):
        if degC is None:
            return None
        return degC + 273.15
    
    def Fahrenheit_to_Kelvin(self,degF):
        if degF is None:
            return None
        return (degF + 459.67) * 5./9.
    
    def Rankine_to_Kelvin(self,degR):
        if degR is None: 
            return None
        return degR * 5./9.
    
    def Kelvin_to_Celsius(self,degK):
        if degK is None:
            return None
        return degK - 273.15
    
    def Kelvin_to_Fahrenheit(self,degK):
        if degK is None:
            return None
        return (degK * 9./5.) - 459.67
    
    def Kelvin_to_Rankine(self,degK):
        if degK is None:
            return None
        return (degK * 9./5.)

    # get pointer to conversion method
    def conversion_method(self,source,target):
        method_name = "{0}_to_{1}".format(source,target)
        return getattr(self, method_name)
        
    def convert(self,source,target,degrees):
        # get path from source to target
        path = self.path(source,target)
        res = None
        last = None

        # iterate through nodes in path
        for step in path:

            # handle first node
            if res == None:
                res = degrees
                source = step.name
                continue

            # remaining nodes
            target = step.name
            if source == target:
                return res
            # call conversion method
            try:
                res = self.conversion_method(source,target)(res)
            except Exception as e:
                print "cannot convert {0} to {1}".format(source,target)
                return None
            source = target
    
        return res

if __name__ == '__main__':
    c = Convert()
    units = ['Kelvin', 'Celsius', 'Fahrenheit', 'Rankine']
    for source in units:
        for target in units:
            if source == target:
                continue
            print '-273.15 degrees ', source, target, c.convert(source,target,-273.15)
            print '0 degrees ', source, target, c.convert(source,target,0)
            print '32 degrees ', source, target, c.convert(source,target,32)
            print '100 degrees ', source, target, c.convert(source,target,100)
            print '212 degrees ', source, target, c.convert(source,target,212)
