class SamplePartition(List[SampleDict], abc.ABC):
    @overload
    def __init__(self, *, training_subset: float = 0.80) -> None:
        ...

    @overload
    def __init__(
        self,
        iterable: Optional[Iterable[SampleDict]] = None,
        *,
        training_subset: float = 0.80,
    ) -> None:
        ...

    def __init__(
        self,
        iterable: Optional[Iterable[SampleDict]] = None,
        *,
        training_subset: float = 0.80,
    ) -> None:
        self.training_subset = training_subset
        if iterable:
            super().__init__(iterable)
        else:
            super().__init__()

    @abc.abstractproperty
    @property
    def training(self) -> list[TrainingKnownSample]:
        ...

    @abc.abstractproperty
    @property
    def testing(self) -> list[TestingKnownSample]:
        ...