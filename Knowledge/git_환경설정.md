# VSCode사용시 깃허브 환경설정
VSCode를 이용해서 깃허브에 관련된 환경설정 할 때 필요한 명령어 모음   

---

### 깃허브 로그인-아이디 비밀번호 저장하기
* git config --global credential.helper store

---

### 깃허브 브랜치가 보이도록 설정하기
* sudo nano ~/.bashrc
(nano 말고도 기타 에디터 가능)   
```
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

export PS1="\u@\h \[\033[32m\]\w\[\033[33m\]\$(parse_git_branch)\[\033[00m\] $ "
```
* 위 내용을 추가하고 터미널을 재시작 한다.
---
