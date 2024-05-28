### jenkins 이미지 다운로드
docker pull jenkins/jenkins

### jenkins 컨테이너 실행
```
docker run -d -p 8180:8080 -v /var/jenkins_home --name jenkins -u root jenkins/jenkins:latest
```
* jenkins/jenkins:latest는 다운로드 받은 이미지에 맞춰 설정한다.

### jenkins 설치
localhost:8180으로 접속. jenkins 컨테이너 포트 설정에 맞춰 포트를 입력한다.

jenkins에 접속하기 위해선 admin 비밀번호가 필요하다.

```
docker logs jeckins
```
jenkins 로그에 비밀번호가 나와있다. 원래는 도커 컨테이너 내부에 접근해 initialAdminPassword 폴더에서 직접 확인해야 한다.

비밀번호를 입력하고 다음 과정을 진행하면 플러그인을 설치한다.
* install suggested plugins - 기본 플러그인 설치로 진행한다.

이후 계정을 생성하면 완료.
