requirement.txt 파일을 통해 파이썬 프로젝트의 패키지 버전을 지정할 수 있다.   
보통 root에 위치시키고 
```python
numpy==1.24.1 
```
형식으로 작성한다.   

만약 버전을 명시하지 않으면 latest로 지정되고, latest는 버전 관리하기에 좋지 않다.

### requirements.txt를 이용한 패키지 설치
터미널에서 pip install -r requirements.txt 커맨드로 작성한 패키지와 해당 패키지에 필요한 패키지가 설치된다.

### requirements.txt를 터미널 커맨드를 이용해 생성하는 방법
* requirements.txt가 작성되지 않은 상황이고, 이미 여러가지 패키지를 설치해 놓았어도 커맨드를 통해 패키지가 작성된 requirements.txt를 만들 수 있다.
* pip freeze 커맨드를 사용하면 패키지와 버전이 명시된 requirements.txt를 생성한다.
```python
pip freeze > requirements.txt
```
