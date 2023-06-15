class Distance:
    """Abstact definition of a distance computation"""

    def distance(self, s1: Sample, s2: Sample) -> float:
        raise NotImplementedError