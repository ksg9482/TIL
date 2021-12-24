# 교차 출처 리소스 공유

교차 출처 리소스 공유(CORS, Cross-Origin Resource Sharing)는 동일 출처 정책(SOP)으로 인해 웹의 상호작용이 제한된 상황에서 동일 출처 정책을 우회하기 위한 방법이다.

서버에 응답을 요청할 때 HTTP 에 새로운 Origin 요청 헤더와 새로운 Access-Control-Allow-Origin 응답 헤더를 추가해서 제공하는 것. 이렇게 추가 헤더를 사용해서 다른 출처의 선택한 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 것이다.

교차 출처 리소스 공유의 종류는 다음과 같다.

### Simple Request

이하의 조건을 만족하는 요청을 Simple Request라고 한다.

- HTTP METHOD: GET, HEAD, POST 일 경우
- 수동으로 설정 가능한 HTTP 헤더: Accept, Accept-Language, Content-Language, Content-Type
- 가능한 Content-Type 종류: application/x-www-form-urlencoded, mulitpart/form-data, text/plain

### Preflight Request

Simple Request 가 아닌 경우 Preflight Request 에 해당한다. 이는 요청을 보내기전에 OPTIONS 메소드 방식으로 먼저 요청하는 것을 말한다.

본격적인 교차 출처 HTTP 요청 전에 서버 측에서 그 요청의 메소드와 헤더에 대해 인식하고 있는지를 체크하는 것이고, 본 요청을 보내기 전에 본 요청에 대한 권한을 확인 하는 작업을 통하여, 본 요청이 유효할 수 있는지 체크한다

동작방식은 이하와 같다.

- 동작방식은 이하와 같다.
- 서버에서 Preflight Request 에 대한 응답
- 서버에 실제 요청을 전송
- 서버에서 실제 요청에 대해 응답

### Credential Request

Http Cookie, Http Authentication 등의 인증된 정보를 인식할 수 있게 하는 요청이다.

Credential Request는 조건에 따라서 Simple Reqeust나 Preflight Request로 나뉘는데, 쿠키나 인증정보를 서버에서 응답하는 경우 해당 정보들에 접근하는 상황이 Credential Request이다.

서버에서 응답 헤더에 Access-Control-Allow-Credentials: true 를 반환함으로써 클라이언트에서 쿠키 접근이 가능해지나, Access-Control-Allow-Origin: * 과 같은 응답은 불가능하다.

### Request without Credential

CORS 요청은 기본적으로 Non-Credential 요청이고, withCredentials 설정을 한 경우에만 Credential 요청이 된다.