from hyppo.independence.base import IndependenceTest



class AreaCoverageIndependenceTest(IndependenceTest):
    coverage_factor_default = 1
    def __init__(self, coverage_factor=coverage_factor_default, **kwargs):
        self.coverage_factor = coverage_factor
        super(AreaCoverageIndependenceTest, self).__init__(**kwargs)
        
    def statistic(self, x, y):
        x,y = rank_transform_unbiased(x,y)
        x=x.reshape(-1,1)
        y=y.reshape(-1,1)
        edge_length = np.sqrt(self.coverage_factor/x.shape[0])
        rectangles = create_clipped_rectangles_around_points(x,y,edge_length)
        min_area_for_n = calc_min_area_for_n(x.shape[0], edge_length)
        RTA = union_rectangles_fastest(rectangles) - min_area_for_n
        return 1- (RTA / (1-np.exp(-self.coverage_factor)-min_area_for_n))
    
    def test(self, x, y,reps=1000,workers=-1):
        return super(AreaCoverageIndependenceTest, self).test(x,y, reps, workers, is_distsim=False)
