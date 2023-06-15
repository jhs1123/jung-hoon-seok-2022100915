class DealingPartition(abc.ABC):
    @abc.abstractmethod
    def __init__(
        self,
        items: Optional[Iterable[SampleDict]],
        *,
        training_subset: tuple[int, int] = (8, 10),
    ) -> None:
        ...

    @abc.abstractmethod
    def extend(self, items: Iterable[SampleDict]) -> None:
        ...

    @abc.abstractmethod
    def append(self, item: SampleDict) -> None:
        ...

    @property
    @abc.abstractmethod
    def training(self) -> list[TrainingKnownSample]:
        ...

    @property
    @abc.abstractmethod
    def testing(self) -> list[TestingKnownSample]:
        ...