class Line:
    def __init__(self, start_point, end_point):
        """
        We assume start and end point are tuples from R^2
        Aka, points of the form (x,y)
        """
        self.start_point = start_point
        self.end_point = end_point
        
    def euclidean_distance(self):
        return math.pow(math.pow(self.end_point[1] - self.start_point[1], 2) + math.pow(self.end_point[0] - self.start_point[0], 2), 0.5)
    
    def absolute_value_distance(self):
        return abs(abs(self.end_point[1] - self.start_point[1]) + abs(self.end_point[0] - self.start_point[0]))

line = Line([2, 3], [4, 7])

#code.interact(local=locals())
