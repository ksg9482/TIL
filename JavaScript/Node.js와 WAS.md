# Node.js와 WAS
Node.js와 WAS의 관계를 알기 위해선 WAS와 WS에 대해 알아야 한다.
### WS (Web Server 웹 서버)
정적파일(html, js, 이미지파일 등)을 제공하기 위한 서버로 HTTP 프로토콜에 의해 제공된다.   
정적파일로만 처리할 수 있는 것들은 WAS로 요청을 넘기지 않고 처리하고, 자체적으로 처리할 수 없는 정보에 대해서는 WAS에 처리를 요청한다.   
요청이 많을 경우 웹 서버에서 웹문서를 WAS에서는 페이지를 양분하여 처리하여 서버의 부담을 줄이는 역할도 가능하다.   
예: apache, nginx 등   
   
### WAS (Web Application Server 웹 어플리케이션 서버)
동적인 데이터를 제공하기 위한 서버. 웹 서버에서 처리할 수 없는 동적인 정보를 처리햐여 웹서버에 정적인 정보를 제공한다.   
일반적으로 웹 서버의 기능을 내재하고 있어 웹 서버가 없이도 서비스가 가능하다.   
WAS와 DB가 연결되어 WAS에서 처리에 필요한 데이터를 꺼내와 원하는 정보로 가공한다.   
   
### WS와 WAS를 나누는 이유
* 데이터 처리방식이 달라 정적 컨텐츠를 WAS에서 처리하여 부하를 줄 필요가 없다.
* 사용자들에게 WAS를 공개할 필요가 없다.(보안)
* 여러대의 WAS를 연결 할 수 있기에, 하나의 웹서버로 여러 웹 어플리케이션 서비스가 가능하다(java서버, python서버, javascript서버 등을 하나의 웹서비스를 통해 서비스 할 수 있다.)
   
### Node.js는 WAS인가?
그렇다면 Node.js는 무엇일까? Node.js와 express로 웹서버를 구성하는데 Node.js는 웹서버라고 볼 수 있는가?   
공식홈페이지에서는 Node.js를 'Node.js는 Chrome V8 JavaScript 엔진으로 빌드된 JavaScript 런타임이다.'라고 소개한다.   
V8 자바스크립트 엔진을 통해 자바스크립트를 브라우저가 아닌 환경에서도 동작하게 만든 것이 Node.js이다.   
이를 'Node.js는 .js로 작성된 Java Script를 읽어 실행해주는 인터프리터 기반 런타임'이라고 표현한다.   
   
즉, Node.js는 런타임이기에 그 자체만으로는 웹서버로 기능할 수 없고 express 프레임워크를 통해 웹서버로 기능하게 된다.   
그러나 Node.js는 스크립트 엔진이라 바이너리 엔진보다 성능이 떨어지고, 많은 이용자의 동시접속과 빠르고 안정적인 속도를 제공해야 하는 웹서버로는 불리할 수 있다.
