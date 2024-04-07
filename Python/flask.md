# flask 기초
### __name__
플라스크 객체를 app에 할당. __name__ 변수에는 해당 모듈의 이름이 저장된다.
* 실행하는 코드쪽에서는 __name__에 __main__가 할당된다.
  * 파일명이 A라도 '__main__'가 할당.
* import로 가져오면 __name__에 모듈명이 할당된다.
  * import명이 ABC라면 'ABC'가 할당. 

### 시작점(entry point)
C, JAVA 같은 언어는 코드를 시작하는 시작점을 가지고 있음
 * public static void main(String[] args) {} 

파이썬은 스크립트 언어. 스크립트 언어는 전통적으로 시작점 없이 스크립트 코드를 바로 시작함.

### flask 객체 생성
Flask(__name__)으로 설정하여 현재 위치를 flask 객체에 알려줘야 함.
 * 이름을 변경해도 실행되지만, 일부 확장 기능 사용시에는 해당 이름을 정확히 알려주지 않을 경우 정상동작하지 않음

### 파이썬 데코레이터
* 파이썬 뿐만 아니라 다양한 언어 전반에 걸쳐 많이 사용됨

### 파이썬 데코레이터를 알기 위한 사전 지식
#### 중첩함수(Nested function)
* 함수 내부에 정의된 또다른 함수
* 중첩 함수는 해당 함수가 정의된 함수 내에서만 반환 가능
  * 함수 안에 선언된 변수는 함수 안에서만 사용 가능한 원리와 동일
* 중첩함수를 함수 밖에서 호출할 수 있는 방법이 있는데, 이를 이해하기 위해 일급 함수, 클로저를 알아야 함
  * 외부 함수의 반환값으로 내부 함수를 반환한다
  * 필요한 값을 미리 넣어둔 함수를 반환하여 추가 데이터를 입력해 기능하게 하는 함수로 반환한다.

#### 일급 함수(First Class Function)
* 변수에 할당 가능
* 함수의 인자로 활용 가능
* 함수의 반환값으로 활용 가능
  
파이썬은 모든것이 객체. 파이썬 함수도 객체로 되어 있어서 기본 함수 기능 이외 객체와 같은 활용이 가능. 즉, 일급 객체(일급 함수)의 조건을 만족함

요즘언어(JS, python, Kotlin)는 보통 지원하는데 C 같은 옛날 언어는 보통 지원 안함

### 클로저
* 함수와 함수가 가진 데이터를 함께 복사, 저장해서 별도 함수로 활용하는 기법
* 외부함수가 소멸해도 외부 함수 안에 있는 로컬 변수 값과 내부함수를 사용할 수 있는 기법

주 사용처

* 일반적으로 제공해야 할 기능(method)이 적은경우
* 제공해야 할 기능이 많으면 class 사용

### 데코레이터
함수 앞 뒤에 기능을 추가해서 다루기 위한 방법
* 데코레이터 함수 내부에서 데코레이터의 대상이 된 함수를 위임하여 실행하는 함수를 구성한다(nested function).
* 인자로 받은 함수가 살아있고 실행된다(closure)
* 래핑함수 함수 안에서 내부함수 앞 뒤에 기능을 추가해서 사용할 수 있다
* 전후처리가 길면 빛을 발함(유효성 검사, 공통 처리 등)
* 본래 함수가 인자가 n개면 데코레이터 내부 함수 인자도 n개 받으면 된다

#### 파라미터와 관계 없이 모든 함수에 적용 가능한 데코레이터 만들기
* 파라미터는 어떤 형태이든 결국 (*args, ***kwargs)로 표현 가능
* 데코레이터 내부 함수의 파라미터를 (*args, ***kwargs)로 작성하면 어떤 함수이든 데코레이터 적용 가능

한 함수에 대해 여러 데코레이터를 사용할 수 있고 나열한 순서대로 실행됨

클래스 메서드에도 데코레이터 사용가능
* 단, 클래스 메서드는 첫 파라미터가 self이므로 데코레이터도 작성시 self를 포함시켜야 함
  * wrapper(self, *args, **kwargs)

#### 데코레이터가 인자를 받게 하려면
* 중첩함수 안에 함수를 받을 함수를 만들고, 그 안에 인자를 받을 함수를 만듦.
  * 중첩함수의 depth를 하나 더 깊게 만든다.
  * 데코레이터 함수 -> 데코레이터 대상인 함수를 받는 함수 -> 데코레이터의 인자를 받는 함수
```python
def decorator1(num):
    # wrapper를 하나 더 두어서 데코레이터가 받는 인자를 처리하도록 한다
    def outer_wrapper(function):
        def inner_wrapper(*args, **kwargs):
            print('decoration1 {}'.format(num))
            return function(*args, **kwargs)
        return inner_wrapper
    return outer_wrapper
```
##### 번외
문자열.format()
* '{0}, {1}, {2}'.format('A', 'B', 'C') -> 'A, B, C'
  * format함수에 입력된 값으로 문자열 괄호의 값을 대체함.
  * format 매핑할 이름에 직접 할당할 수 도 있음 ('{a}, {b}'.format(a='aaaa', b='bbbb'))

### routing 방법
##### 기본
```python
@app.route("/")
def hello() {
    return "<div>hello<div>"
}
```
* app.route를 바로 쓰면 기본적으로 GET 메서드

##### 파라미터 받기
```python
@app.route("/profile/<username>")
def get_profile(username) {
    return "profile: " + username
}
```
* @app.route()의 인수의 괄호(<>)로 파라미터를 받음
* 함수의 인수와 동일한 변수명이여야 한다

##### 타입을 지정한 파라미터 받기
```python
@app.route("/profile/<int:user_id>")
def get_user(user_id) {
    return "user_id: " + user_id
}
```
* 괄호(<>)안에 타입을 먼저 지정하고 변수명을 선언할 경우 해당 변수는 지정한 타입으로 취급됨. 아무것도 안하면 기본 str
* "user_id: %d" % user_id - 문자열 내부에 %d를 두어서 매핑된 값으로 치환할 수 있음
  * %d: int
  * %f: float
  * %s: string
* 만약 profile/abc 식으로 숫자가 아니라 문자열을 입력하면 int로 변환되지 않아 /profile/<int:user_id>에 접근할 수 없다.

### flask로 정적페이지 로드
* flask 하위 template 폴더에 html 위치.
* render_template('file.html')함수를 통해 html을 렌더해서 전송

#### flask로 정적페이지 로드시 경로를 찾지 못할 때
* 가장 합리적인 방법은 static_url_path을 flask 객체 생성시 선언해 주는 것
  * app = Flask(__name__, static_url_path='/static')
  * static 폴더에 CSS등 정적파일 위치 표시
    * template는 그대로 사용
  * 서버에 있을 때와 웹에서 로드 되었을 때 서로 파일 위치가 달라짐
  * static_url_path가 /static이니 src도 path 시작을 static으로 한다

### jinja2
파이썬 템플릿 엔진

다음 2가지 문법이 핵심
* {{변수명}}
* {%파이썬 코드%}

#### 반복문
* {% for %} {% endfor %}
* for로 시작해서 endfor로 끝난다. 블록 안에서는 들여쓰기 안해도 됨
```python
{% for value in values %}
<li>{{ value }}</li>
{% endfor %}
```
* values 길이 만큼 value가 반복해서 생성된다

#### python 반복문 문법과 다른점
```python
<ul>
    {% for index in range(values | length) %}
        <li>{{ values[index] }} {{ loop.index }}</li>
    {% endfor %}
</ul>
```
* range() - 파이썬과 동일
* len(values) - values | length 로 작성
  * <iterable> | length 방식.
* 반복문 인덱스 - loop.index
  * 반복문의 반복 횟수 가져옴
* values[index] - python과 동일

#### 조건문
{% if %} {% elif %} {% else %} {% endif %}
* 들여쓰기 안해도 됨

#### 주석 
{# #}
* \# 블럭 안에 넣기

#### flask에서 cors 지원
* cors는 request 뿐만아니라 response에도 cors 헤더가 있어야 함.
* flask가 cors 처리 함수 제공해줌
```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
```
CORS에 app을 인자로 넣으면 요청, 응답 객체에 cors 지원 헤더를 삽입해준다.

#### api response로 json 반환
make_response()함수 이용.
* (value_dict, status_code) 인수로 이용
* jsonify(key=value) or jsonify({key:value}) 형식으로 값 입력

```python
@app.route("/path/to", method=["GET", "POST", "PUT", "DELETE"])
```
* GET, PUT, DELETE와 POST 메서드 때 파라미터 값을 추출하는 방식 다름
* GET, PUT, DELETE
  * request.args.get('name')
*POST
  * request.get_json()
  * body에서 꺼냄
  * 변수에 넣어서 key 호출

### 에러 핸들링
* errorhandler를 이용해서 에러 처리
  * return의 두번째 인자로 에러코드로 넘겨주지 않으면 200 성공으로 인지
```python
@app.errorhandler(404)  # 없는 페이지를 요청했을 때의 에러
def page_not_found(error):
    return "<h1>404 Error</h1>", 404
```
### 로깅
logging 라이브러리 이용
* flask 전용은 아니고 기본 제공 라이브러리. flask에서도 많이 씀
* 로깅 라이브러리 이용시 파일화 하는 log level을 바꾸고 싶으면 거의 터미널 단위로 재실행 해야함.
  * 맨처음 실행시 환경수준에서 설정되는 것으로 추정
```python
import logging
# 파일로 남기기 위해서는 filename='test.log' 파라미터, 어느 로그까지 남길 것인지
logging.basicConfig(filename='test.log', level=logging.ERROR)

logging.debug("debug")
logging.info("info")
logging.warning("warning")
# level=logging.ERROR 지정시 여기부터 파일화
logging.error("error")
logging.critical("critical")
```
#### 로깅핸들러
* FileHandler - 파일로 로그를 저장
* RotatingFileHandler - 파일로 로그를 저장하되 정해진 사이즈를 넘으면 새 파일로 생성
  * maxBytes - 하나의 파일 사이즈
  * backupCount - 파일 갯수
일반적으로 RotatingFileHandler 사용

### 기타 데코레이터
```python
@app.before_first_request
```
* 기동 후 가장 처음 들어온 HTTP 요청에만 실행.

```python
@app.before_request
```
* HTTP 요청이 들어올 때마다 실행

before_first_request, before_request 는 인자를 전달할 수 없다

```python
@app.after_request
```
* 독특함. HTTP 요청 처리가 끝나고, 응답하기 바로 직전에 실행
* api에 매핑된 함수 처리 -> after_request 처리 순
* response를 리턴해야 함
* 호출 추적하면서 로그 작성할 때 쓰는 건가?
