# Cookie
## 쿠키(Cookie)란?
* HTTP 통신 시 사용자 정보를 유지하고자 서버에서 생성해 응답 헤더에 붙혀 클라이언트에 전송한다. 쿠키는 클라이언트의 로컬디스크에 파일형태 또는 메모리에 저장된다.
* 쿠키의 특징
  * 일반 텍스트 형식이다. 
  * 각 브라우저당 300개, 각 호스트 마다 20개 까지 허용한다.
  * 일반적으로 최대 크기는 4KB이다.(브라우저 마다 다르다)
* 쿠키의 용도
  * 토큰을 저장한다.
  * 클라이언트 관리에 필요한 정보를 저장한다.
  * 임시데이터를 관리하는 데 사용한다.

## 쿠키의 속성
* Domain - 웹 브라우저가 쿠키값을 전송할 서버의 도메인
* Path - 웹 브라우저가 쿠키값을 전송할 URL을 지정
* Expires - 쿠키의 유효기간
* Secure - SSL 통신 채널 연결 시에만 쿠키를 전송하도록 설정한다
* HttpOnly - 서버 요청이 있을 때에만 쿠키가 전송되도록 하고, 임의로 웹브라우저에 출력되지 않게 설정한다

## 쿠키의 보안 속성
### Secure
웹브라우저와 웹서버가 HTTPS로 통신하는 경우에만 쿠키를 전송하는 옵션이다. 네트워크에서의 데이터 탈취를 예방하기 위해 HTTP의 보안을 강화한 HTTPS를 사용하는데,   
개발자의 부주의로 HTTP를 통해 데이터를 보내 쿠키가 유출되는 경우가 있다. 이를 예방하기 위해 Secure Cookie 옵션을 사용하여  HTTPS가 아니면 쿠키를 전송하지 않도록 한다.

### HTTP Only
document.cookie등 클라이언트에서 자바스크립트를 통한 쿠키 탈취를 예방하기 위한 옵션이다.   
브라우저에서는 HTTP Only가 설정된 쿠키를 조회 할 수 없고, 서버로 HTTP 요청을 보낼때만 쿠키를 전송한다.   
이를 통해 XSS(Cross Site Scripting)공격을 차단할 수 있다.   
   
* XSS공격 - 서버측에서 제공하는 스크립트가 아니라 권한이 없는 사용자가 웹사이트에 스크립트를 삽입해 의도치 않은 동작을 일으키는 공격.

#### HTTP ONLY의 한계점
SPA(Single Page Application)로 구현된 웹사이트는 한 페이지에서 많은 기능을 수행하기 위해 AJAX를 통해 서버와 통신한다.   
만약 AJAX통신을 할 때 cookie값을 서버에 전송해야 한다면 HTTP Only옵션이 적용된 cookie는 자바스크립트를 통해 접근 할 수 없다.   
접근하려면 설정을 해체해야 하고 이는 XSS공격에 취약점이 된다. 즉, SPA환경에서는 사용에 제약이 있다.

