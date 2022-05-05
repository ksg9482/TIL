# RESTful

## REST(Representational State Transfer)란?
자원(resource)을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고받는 모든 것을 의미한다.   
즉, 자원의 표현에 의한 정보전달이다.   
* 자원은 해당 소프트웨어가 관리하는 모든 것이다.
* 표현은 그 자원을 표현하기 위한 이름이다.
* 정보 전달은 데이터가 요청되는 시점에서 자원의 상태(정보)를 전달한다.

### REST는 자원, 행위, 표현으로 구성되어 있다.
* 자원
  * server에 있는 모든 자원에는 고유한 ID가 존재한다
  * 자원을 구별하는 아이디는 HTTP URI이다
  * client는 URI를 이용해 자원을 지정하고 해당 자원의 상태(정보)에 대한 조작을 server에 요청한다

* 행위
  * HTTP 프로토콜의 Method를 사용한다
  * HTTP 프로토콜은 GET, POST, PUT, DELETE Method를 제공한다

* 표현
  * client가 자원에 대한 조작을 요청하면 server는 적절한 응답(Representation)을 보낸다
  * JSON 또는 XML로 데이터를 주고 받는 것이 일반적이다
   
### 구체적으로는?
HTTP URI를 통해 자원을 명시하고, HTTP Method를 통해 해당자원에 CRUD를 적용한다.   
리소스를 활용하기 위한 구조로서 REST가 지향하는 서비스구조를 자원 기반의 구조(ROA, Resource Oriented Architecture)라고 한다.   
설계의 중심에 자원이 있고 HTTP Method를 통해 자원을 처리하도록 한 설계이다.   

#### CRUD
* Create : 생성(POST)
* Read : 조회(GET)
* Update : 수정(PUT)
* Delete : 삭제(DELETE)
* HEAD: header 정보 조회(HEAD)


### REST가 필요한 이유?
다양한 브라우저, 클라이언트, 모바일 등 멀티 플랫폼에 대해 지원 해줘야 한다. 


### REST 특징
REST는 HTTP 프로토콜을 그대로 활용하기 때문에 웹의 장점을 최대한 이용할 수 있다
* Client - Server 구조
  * 자원을 요청하는 쪽이 client, 자원이 있는 쪽이 server이다.
  * 책임지는 영역이 다르기 때문에 서로간 의존성이 줄어든다.
* Stateless 무상태성
  * HTTP 프로토콜은 stateless하므로 REST 역시 stateless하다.
  * server는 각각의 요청을 완전히 별개의 것으로 인식하고 처리한다. 즉, 이전 요청이 다음 요청의 처리에 연관되선 안된다.
* Cacheable 캐시 처리 기능
  * HTTP 프로토콜을 그대로 사용하므로 웹에서 사용하는 기존의 인프라를 활용할 수 있다.
  * 캐시 사용을 통해 응답시간의 이득을 얻고 REST server 트랜잭션이 발생하지 않게 할 수 있다.
* Layered System 계층화
  * client는 REST API server만 호출한다
  * REST Server는 다중계층으로 구성될 수 있다. 즉, API Server는 순수 비즈니스 로직을 수행하고 그 앞단에 보안, 로드밸런싱등을 추가하여 구조에 유연함을 줄 수 있다
* Code-On-Demand(optional)
  * Server로부터 스크립트를 받아서 Client에서 실행한다.
  * 반드시 충족할 필요 없다
* Uniform Interface 인터페이스 일관성
  * URI로 지정한 자원에 대한 조작을 통일되고 한정적인 인터페이스로 수행한다
  * HTTP 프로토콜을 따르는 모든 플랫폼에서 사용 가능하기에 특정 언어나 기술에 종속되지 않는다 

## API(Application Programming Interface)란?
API는 사용자가 원하는 것을 시스템에 전달할 수 있게 지원하여 시스템이 이 요청을 이해하고 이행하도록 할 수 있다.   
즉, 데이터와 기능의 집합을 제공해 컴퓨터 프로그램간 상호작용을 할 수 있게 한 것이다.   
   
REST API란 REST 기반으로 서비스API를 구현 한 것이다.   
   
### REST API 설계 규칙

* URI는 정보의 자원을 표현해야 한다.
* 자원에 대한 행위는 HTTP Method로 표현한다.
  * 단,URI에 HTTP Method, CRUD기능을 나타낸 표현이 들어가면 안된다.
  * 경로중 변하는 부분은 유일한 값(:id)으로 대체한다.(DELETE /member/:id)
* 슬래시 구분자(/)는 계층 관계를 나타내는데 사용한다.
* URI 마지막 문자로 슬래시(/)를 포함하지 않는다.
  * 분명한 URI를 만들어 통신을 해야하기 때문에 혼동을 주지 않기 위함이다.
* 하이픈(-)은 URI 가독성을 높이는데 사용한다.
* 밑줄(_)은 URI에 사용하지 않는다.
  * 보기 어렵거나 밑줄 때문에 문자가 가려지기도 하므로 가독성을 해칠 수 있다.
* URI 경로에는 소문자가 적합하다.
  * RFC3986(URI 문법 형식)은 URI 스키마와 호스트를 제외하고는 대소문자를 구별한다.
* 파일 확장자는 URI에 포함하지 않는다.
  * Accept header를 이용한다
* 리소스 간에 연관관계가 있는 경우 '/리소스명/리소스ID/관계 있는 다른 리소스명'을 사용한다.


# RESTful이란?
일반적으로 REST라는 아키텍처를 구현하는 웹서비스를 나타내는 용어이다.   
즉, REST API를 제공하는 웹서비스를 RESTful하다고 한다.   
   
RESTful은 REST를 REST답게(REST API 설계 규칙을 준수하도록) 쓰기위한 방법이다.    


