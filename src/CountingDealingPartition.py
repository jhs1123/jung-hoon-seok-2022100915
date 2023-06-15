class CountingDealingPartition(DealingPartition):
    def __init__(
        self,
        items: Optional[Iterable[SampleDict]],
        *,
        training_subset: tuple[int, int] = (8, 10),
    ) -> None:
        self.training_subset = training_subset
        self.counter = 0
        self._training: list[TrainingKnownSample] = []
        self._testing: list[TestingKnownSample] = []
        if items:
            self.extend(items)

    def extend(self, items: Iterable[SampleDict]) -> None:
        for item in items:
            self.append(item)

    def append(self, item: SampleDict) -> None:
        n, d = self.training_subset
        if self.counter % d < n:
            self._training.append(TrainingKnownSample(**item))
        else:
            self._testing.append(TestingKnownSample(**item))
        self.counter += 1