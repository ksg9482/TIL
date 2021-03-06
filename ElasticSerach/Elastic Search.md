# ElasticSearch
Elasticsearch는 분산형 RESTful 검색 및 분석엔진으로 Elastic Stack의 중심에 위치한다.
그중 Elasticsearch는 검색, 분석, 데이터 저장소 역할을 한다.
엘라스틱은 빠른 속도, 확장성, 복원성, 정형-비벙형 데이터를 모두 수용할 수 있다.

### RDB와 엘라스틱 서치의 차이?
* RDB는 행을 기반으로 데이터를 저장한다. 반대로 엘라스틱서치는 단어를 기반으로 데이터를 저장(역인덱스, inverted index)한다.
* RDB는 데이터 수정, 삭제의 편의성과 속도 면에서 강점이 있지만 다양한 조건의 데이터를 검색하는데 구조적 한계가 있다.
도큐먼트의 개수만큼 확인을 반복하기 때문에 수가 많을 수록 비효율적이게 된다.

* 엘라스틱 서치는 단어기반으로 데이터를 저장하기 때문에 특정 단어가 어디 저장되어 있는지 이미 알고 있다. 
한번의 조회로 해당하는 단어가 어느 도큐먼트에서 쓰였는지 검색할 수 있다.
* 그러나 수정과 삭제는 엘라스틱 서치 내부적으로 많은 리소스가 소요된다.    
이 점이 엘라스틱 서치가 RDBMS를 완전히 대체할 수 없는 중요한 이유고, 데이터 특성상 수정과 삭제가 많을 경우 RDB와 엘라스틱 서치 영역을 나누어 구조를 짜야한다.

기존 DBMS와는 달리 Elastic Search는 NoSQL기반, 검색엔진에서 나왔기 때문에 데이터의 유형, 검색조건, 시각화 여부 등 적절한 모델링을 적용해야 한다.
Elastic Search에서 관계형 데이터 모델링 방법은 크게 4가지가 있다.


### 관계형 데이터 모델링 방법

#### 1) Parent-Child 모델링
엘라스틱서치가 제공하는 Join data type을 바탕으로 설계한다.   
Join type으로 Parent, Child를 구분하고 같은 라우팅 ID를 키로 제공하여 같은 샤드(Shard)에 위치하게끔 설계한다.   
전체 도큐먼트에서 업데이트와 삭제가 빈번하고 1:N 관계일 때 고려할 만 하다.   

#### 2)Nested 모델링
엘라스틱서치에서 Nested data type을 활용해 설계하는 방법이다.    
하나의 인덱스에서 Nested data type을 선언하고 오브젝트 속성들을 정의하여 연속(Array)하게 배치하는 방식.   
두 개 이상의 속성을 가진 오브젝트를 배열(Array) 구조로 표현해야 할 때 고려할 만 하다.   

#### 3)Application Side Join 모델링
기본 키(Primary Key)를 기준으로 관계(Relation) 있는 엔티티(Entity)들을 서로 다른 도큐먼트에 배치하여   
Application side에서 키를 기준으로 조인(Join)하여 처리하는 방식이다.   
1:1 관계의 구조로 기존 쿼리와 집계(Aggregation)를 그대로 사용해야 할 때 고려할 만 하다.   

#### 4)Denormalization 모델링
데이터 전체를 비정규화하여 인덱싱하는 방법으로 각 데이터의 중복을 허용하여 조인(Join)이 필요하지 않도록 한다.   
쿼리 시점에서 최고의 성능을 낼 수 있으나 공통 필드의 변경이 잦거나 한정된 물리 서버로 구성해야 한다면 유의해야 한다.
