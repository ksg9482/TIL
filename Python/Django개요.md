### 장고를 쓰는 이유
* 많은 기능들이 이미 내장되어 있기 때문에 불러오면 된다.
* 보안 등 안전을 위한 기능들도 포함되어 있다.
* 아키텍처들이 서로 비의존적이라서 원하는 곳, 원하는 때 불러올 수 있다.


### 기본 아키텍처
유저 -> 웹서버 -> urls.py -> view -> model -> view -> 웹서버 -> 유저
* 유저가 웹서버 url로 요청을 보낸다.
* urls.py는 해당 url이 유효한 url인지 확인하고 view에 연결.
* view는 Data 입출력 및 처리가 필요할 경우 model에 연결.
  * template은 view의 ui를 담당한다.
* model에서 처리가 끝나면 view로 반환.
* view는 유저에게 요청에 해당하는 결과를 반환.
   
model-view-template로 이어지는 패턴이 MVT패턴이다.(MVC패턴 친척)
### 설치 및 시작
* pip install django
* django-admin staerproject <프로젝트 이름>
### 가상환경
Python은 가상환경을 만들어 사용하는 것이 원칙이다.
* sudo apt install python-virtualenv
  * 가상환경 설치
* virtualenv venv
  * 가상환경을 작동하는 폴더 생성. 원하는 django 프로젝트 폴더에서 커맨드 입력
  * 의존성이 프로젝트 폴더로 한정되기 때문에 프로젝트 별로 관리 할 수 있음
* source venv/bin/activate
  * 가상환경을 동작시키는 커맨드. 중지는 deactivate
