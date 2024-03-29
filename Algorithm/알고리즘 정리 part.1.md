# 데이터 구조
___
### 알고리즘과 데이터구조 개요
알고리즘이란 간단하게 말하면 문제를 해결하기 위한 논리적 단계이다. 알고리즘은 자연어, 코드등으로 표현할 수 있는데 어렵고 이해하기 힘든 알고리즘 보다 간단하고 이해하기 쉬운 알고리즘이 더 강력하고 유용하다.

데이터구조와 알고리즘은 서로 다른 개념이면서 상호 보완적이다. 데이터구조는 알고리즘이 다루는 데이터를 구성하며 알고리즘이 데이터를 처리하고 원하는 정보를 산출하는 과정에서 필요한 부분을 담당한다.

함수는 입력을 받아 어떤 처리과정을 수행한 후 출력한다. 함수는 매개변수(파라미터) 또는 인수라고 하는 데이터를 입력으로 사용하며 때로는 결과를 반환한다. 프로그래밍에서의 함수는 입력이 있어도 출력이 없을 수 있다. 이를 void함수라 한다.

* 매개변수: 함수를 정의할 때 사용하는 변수
* 인수: 함수를 호출하며 전달하는 매개변수의 실제 값

재귀는 실행도중 자기 자신을 호출하는 것이다. 보통 특정 조건을 만족할 때 까지 끊임없이 동작하는데, 컴퓨터의 메모리는 한계가 있으므로 최대 재귀 깊이를 초과하면 스택 오버플로우 에러가 발생 할 수 있다.

반복은 재귀와 혼동해서는 안되는 또 다른 개념으로, 특정 조건을 충족할 때까지 코드 덩어리의 실행이 되풀이되는 것을 뜻한다.

### 알고리즘의 세가지 유형

* 분할 정복 알고리즘: 큰 문제를 여러개의 작은 문제로 나눠 해결하고 결과를 결합해 하나의 해결방법을 얻는다.
* 탐욕 알고리즘: 실행되는 순간마다 최상의 결정을 내린다. 그러나 문제 전체를 해결하는 최적의 결정일지는 장담할 수 없다.
* 동적 프로그래밍 알고리즘: 과거에 내린 결정이 앞으로의 결정에 영향을 준다. 다양한 해결방법을 찾아 저장한 후 나중에 재사용한다.

탐욕 알고리즘은 근사치를 구하는데 유용하고, 동적 프로그래밍 알고리즘은 최적화 하는데 유용하다.

### 알고리즘 분석
알고리즘의 효율성을 분석할 때는 시간 복잡도와 공간 복잡도를 이용한다.
* 시간 복잡도: 주어진 입력에 따라 알고리즘이 문제를 해결하는데 걸리는 시간
* 공간 복잡도: 알고리즘이 문제를 해결할 때 점유하는 컴퓨터 메모리

가장 자주 사용되는 것은 시간 복잡도이며, 공간 복잡도는 자원이 제한된 시스템에서 프로그램이 구현하는 것과 같이 특별한 경우에 사용한다.

알고리즘의 효율성을 수학적으로 판단하는 방법은 최악의 경우, 최상의 경우, 평균을 측정하는 등 여러가지가 있다. 이런 효율성을 설명할 때는 보통 빅 오 표기법을 이용한다.

### 빅 오 표기법
빅 오 표기법을 이 이름으로 부르는 이유는 대문자 O가 시간 복잡도의 정도를 나타내는 표기법인 차수(Order)를 뜻하기 때문이다. 이 관례가 굳어지면서 자연스레 빅 오 표기법이라 불리게 되었다.

빅 오 표기법은 알고리즘의 실행 시간이 최악인 경우를 상정한다. 주로 다음과 같이 분류한다.
* O(1): 상수형 알고리즘. 데이터 입력량과는 무관하게 실행 시간이 일정하다.
* O(n): 선형 알고리즘. 데이터 입력량에 비례해 실행 시간이 늘어난다. 
* O(log n): 로그형 알고리즘. 시간이 선형적으로 증가하면 n이 기하급수적으로 증가한다. 데이터 입력량이 늘어날수록 단위 입력당 실행시간이 줄어든다.
* O(n log n): 선형 - 로그형 알고리즘. 데이터 입력량이 n배 늘어나면 실행 시간이 n배 조금 넘게 늘어난다.
* O(n^2): 2차 알고리즘. 데이터 입력량의 제곱과 비례하여 실행 시간이 늘어난다. 
* O(2^n):  지수형 알고리즘. 데이터 입력이 추가될 때마다 실행 시간이 2배로 늘어난다.
* O(n!): 팩토리얼(계승)형 알고리즘. 데이터 입력이 추가될 때마다 실행시간이 n배로 늘어난다.

알고리즘 성능은 좋은 순서대로 다음과 같다.
* O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n), O(n!)

# 선형 데이터 구조

데이터 구조가 선형이라는 것은 데이터 구조를 구성하는 요소들이 서로 인접해 순차적인 방식으로 정렬되어 있음을 뜻한다. 가장 일반적인 선형 데이터 구조는 배열과 리스트이다. 

### 배열
배열은 자료형이 같은 요소들을 저장한다. 배열에 저장된 각각의 자료를 요소(element)라고 하며, 0부터 번호가 매겨진다. 
요소에 매겨진 숫자를 배열의 인덱스(index)라고 하는데 배열의 요소는 순차적으로 또는 연속적으로 정렬되어 있다.

그러나 순차적으로 구성되어 있기에 배열에 데이터를 추가하거나 삭제할 때 배열을 재배치 해야 하므로 많은 시간이 걸릴 수 있다. 

대부분의 프로그래밍 언어에서는 배열에 메모리를 할당하기 전에 배열 크기를 지정해야 한다.

1차원 배열은 각 인덱스가 가리키는 요소가 단일 행 또는 단일 열을 나타낸다. 반대로 다차원 배열은 요소가 배열로 이루어진 배열이며 2차원 배열이 가장 일반적인 다차원 배열이다. 2차원 배열은 가장 일반적인 다차원 배열이며 여기에 데이터를 저장한 것을 행렬이라 한다.

### 리스트
리스트의 요소는 흩어진 상태로 메모리에 저장된다. 리스트의 요소는 데이터 요소와 포인터의 한 쌍으로 구성되며 포인터는 리스트 내의 다음 요소를 가리킨다. 어떤 데이터 요소에 접근하려면 바로 이전 요소의 포인터를 사용해야 한다.

데이터 요소와 포인터의 쌍을 노드라고 부르고, 해당 리스트에 진입할 수 있는 진입점을 헤드라고 부른다.

* 단방향 연결 리스트: 노드 하나가 다른 노드를 가리키는 포인터 하나를 갖는다. 마지막 노드의 포인터는 null 값을 갖는다.

* 양방향 연결 리스트: 각 노드가 다음 노드를 가리키는 포인터 하나와 이전 노드를 가리키는 포인터 하나를 갖는다. 데이터를 삭제하거나 리스트를 양방향으로 순회할 때 효율적이다.

* 순환 연결 리스트: 마지막 노드의 포인터는 첫번째 노드를 가리키기에 null 값을 갖지 않는다. 버퍼링과 관련된 용도로 많이 사용된다.

### 스택
추가된 요소를 메모리의 가장 앞 주소에 배치한다. 스택의 최상단에서만 삭제 및 추가를 할 수 있기에 스택에서 특정 요소를 검색하는데 속도가 제한된다. 

데이터 구조의 크기나 규모가 고정된 정적 스택과 실행중에도 크기를 늘릴 수 있는 동적 스택으로 나눌 수 있다. 

역추적, 문자 반전, 함수호출, 스케줄링 등에 사용된다.

### 큐
각 요소에 우선순위를 부여하는 데이터 구조의 한 종류. 큐에 요소를 추가하면 큐의 맨 뒤쪽에 배치된다. 

#### 우선순위 큐
우선순위 큐는 기본적인 큐를 확장한 것으로 키-값 체계를 사용해 큐의 요소를 정렬한다. 모든 요소는 우선순위가 있으며 이는 키에 해당하고, 우선순위가 높은 요소는 우선순위가 낮은 요소보다 큐에서 먼저 삭제 된다. 

우선순위 큐는 일부 알고리즘과 데이터 압축, 네트워킹, 컴퓨터 과학 분야의 응용프로그램에서 사용된다.
