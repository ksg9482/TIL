기본적으로 Ubuntu를 처음 설치할 때 SSH를 통한 원격 액세스는 허용되지 않는다.

### SSH 서비스 설치
```
sudo apt update
sudo apt install openssh-server
```

### SSH 서비스 실행 확인
```
sudo systemctl status ssh
```

### 방화벽을 SSH 통신이 허용되도록 변경
```
sudo ufw allow ssh
```

### SSH 접속
포트를 따로 지정했을 경우 -p 옵션으로 포트번호를 명시한다.
```
ssh username@ip_address
ssh -p <port> username@ip_address
```
