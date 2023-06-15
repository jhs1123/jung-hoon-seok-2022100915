class Chebyshev(Distance):
    """
    Computes the Chebyshev distance between two samples.
    ::
        >>> from math import isclose
        >>> from model import TrainingKnownSample, UnknownSample, Chebyshev
        >>> s1 = TrainingKnownSample(
        ...     sepal_length=5.1, sepal_width=3.5, petal_length=1.4, petal_width=0.2, species="Iris-setosa")
        >>> u = UnknownSample(**{"sepal_length": 7.9, "sepal_width": 3.2, "petal_length": 4.7, "petal_width": 1.4})
        >>> algorithm = Chebyshev()
        >>> isclose(3.3, algorithm.distance(s1, u))
        True
    """

    def distance(self, s1: Sample, s2: Sample) -> float:
        return max(
            [
                abs(s1.sepal_length - s2.sepal_length),
                abs(s1.sepal_width - s2.sepal_width),
                abs(s1.petal_length - s2.petal_length),
                abs(s1.petal_width - s2.petal_width),
            ]
        )