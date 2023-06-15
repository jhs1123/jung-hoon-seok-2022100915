[프로젝트 설명]
Sample : Sample클래스의 인스턴스는 작업 데이터의 핵심 부분이다.

KnownSample : KnownSample의 객체는 확장된 Sample이다. KnownSample은 분류돼어 할당된 종이라는 속성이 Sample에 추가된 것이다.

TriningData : TrainingData 클래스는 데이터 샘플의 두 가지 리스트(모델 학습에 사용되는 리스트와 모델 테스트에 사용되는 리스트)가 있는 컨테이너이다.

Hyperparameter : Hyperparameter 클래스는 고려해야 할 최근접 이웃의 수를 정할 때 사용되는 k값을 가지고 있다. 또한, 이 k값을 사용한 테스트의 요약도 속성으로 가지게 된다.
품질은 얼마나 많은 테스트 샘플이 정확히 분류됐는지 알려준다.

TrainingKnownSample, TestingKnownSample : KnownSample 클래스에서 만들어진 새 하위 클래스.

SampleReader : SDV DictReader 인스턴스가 읽은 입력 필드로부터 Sample 상위 클래스의 인스턴스를 빌드한다.

BadSampleRow : BadSampleRow 클래스를 통해 고유한 예외를 정의한다. (float()에 의한 ValueError 예외 신호를 애플리케이션의 BadSampleRow 예외에 매핑) 

UnknownSample : Unknown 인스턴스는 사용자 분류에 사용될 수 있따. 여기서 분류 메서드인 classify()는 purpose 속성에 의존하지 않고 항상 분류를 수행한다.

Purpose : 코드에서 사용할 수 있는 세가지 객체인 Purpose.Classification, Purpoose.Testing, Purpose.Training이 있는 네임스페이스를 만들어 테스트 샘플을 식별한다.

SamplePartition : __init__()메서드에 대해 두 개의 오버로드를 정의했다. 첫 번째 오버로드는 위치 매개변수가 없는 __init()이고 이것으로 SampleDict 객체의 빈 리스트가 생성된다. 
두 번째 오버로드는 SampleDict객체의 반복 가능한 소스를 유일한 위치 매개변수로 갖는 __init__()이다.

ShufflingSamplePartition : random.shuffle() 메소드를 사용해 샘플이 정확히 한번 섞이도록 한다.

DealingPartition : SampleDict 객체에 대해 테스트와 학습 중 하나를 임의로 선택하는 SamplePartition의 하위 클래스.

CountingDealingPartition : DealingPartition을 확장해 두 개의 내부 컬렉션을 래핑하는 구상 하위 클래스.

Sample 클래스, unknown 클래스, TrainingKnownSample 클래스, TestingKnownSample 클래스, Hyperparameter 클래스는 데이터클래스(@dataclass)로 구현되었다.

*거리와 관련된 클래스들*
Distance : Distance 클래스는 일반적인 거리 개념을 정의하는 기본 클래스 이다.

ED : ED클래스는 Distance 클래스의 하위 클래스로 샘플들간의 유클리드 거리를 측정하는 클래스이다.

MD : MD클래스는 Distance 클래스의 하위 클래스로 샘플들간의 맨해튼 거리를 측정하는 클래스이다.

CD : CD클래스는 Distance 클래스의 하위 클래스로 샘플들간의 체비쇼프 거리를 측정하는 클래스이다.

SD : SD클래스는 Distance 클래스의 하위 클래스로 샘플들간의 쇠레센 거리를 측정하는 클래스이다.


[소감]
아이리스 꽃종 분류기 개발 과제를 해결하기 위해서 교재인 파이썬 객체지향 프로그래밍 4/e를 정독하고 교재의 소스파일들을 찾았습니다. 
이러한 과정들을 통해서 한가지 기능을 코드로 구현하는데에도 많은 방법이 있고 이를 최대한 효율적이게 만드는 것이 프로그래머의 중요한 역량이라는 것을 느낄 수 있었습니다.
사례연구의 코드를 구현하는 것은 저에게 난이도가 있었지만 객체지향 프로그래밍의 실제 사례 코드를 구현할 수 있는 경험이였습니다. 
그리고 이를 토대로 추후 관련 전공수업을 듣거나, 코드를 만들게 될때 저에게 큰도움이 될 것 같습니다.
