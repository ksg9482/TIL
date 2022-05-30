# URI와 URL
### URI
URI는 식별자이다. 특정 리소스를 식별하는 통합 자원 식별자(Uniform Resource Identifier)의미한다.   
웹기술에서 사용하는 논리적 또는 물리적 리소스를 식별하는 고유한 문자열 시퀸스로 인터넷에 있는 자원을 나타낸다.   

### URL
URL는 위치지정자를 뜻한다. 흔히 웹주소를 말하는데 컴퓨터 네트워크 상에서 리소스가 어디 있는지 알려주기 위한 규약이며 URI의 서브셋이다.
___
즉, URI는 식별하고, URL은 위치를 가르킨다.   
URI가 URL의 상위개념이므로 URI는 URL을 포함한다. 그러나 URL은 URI는 아니다.   

### URI의 구조
scheme:[ //[ user [ :password ] @ ] host [:port] ] [/path] [?query] [#fragment]   
   
http:// example.com:8042/over/there?name=farret#nose 일 경우   

http <b>(scheme)</b>   
://example.com:8042/ <b>(authority)</b>   
over/there <b>(path)</b>   
?name=farret <b>(query)</b>   
#nose <b>(fragment)</b>

* scheme: 사용할 프로토콜. 웹에서는 http 또는 https를 사용
* user, password: 서버에 있는 데이터에 접근하기 위한 사용자의 이름과 비밀번호
* host, port: 접근할 대상(서버)의 호스트 명과 포트번호
* path: 접근할 대상(서버)의 경로에 대한 상세 정보
* query: 접근할 대상에 전달하는 추가적인 정보(파라미터)
* fragmant: 메인 리소스 내에 존재하는 서브리소스에 접근할 때 이를 식별하기 위한 정보.
