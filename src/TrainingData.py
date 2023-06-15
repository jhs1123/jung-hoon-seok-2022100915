@dataclass
class TrainingData:
    testing: List[TestingKnownSample]
    training: List[TrainingKnownSample]
    tuning: List[Hyperparameter]