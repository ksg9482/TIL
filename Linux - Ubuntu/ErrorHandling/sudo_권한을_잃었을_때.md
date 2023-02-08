# sudo 권한을 잃었을 때
### 발단:
sudoers를 chmod 777 설정하려고 했다. 나중에야 visudo를 써야한다는 것을 알았는데 당시엔 모르고 변경했기에 발생했다.

### 과정:
이후 sudo명령어를 사용하려고 했는데 위 오류로 인해 사용할 수 없었다. sudoers에 뭐가 들어있길래 망가졌는지 확인하려고 했으나 비밀번호 입력 시도부터 실패한 것이다. 
그제서야 상황의 심각함을 알고 해결방법을 찾았고 터미널창을 2개 사용하는 방법을 사용하기로 했다.

### 해결:
 * 첫번째 터미널에서 echo $$
 * pid 숫자가 나오면 그 숫자를 이후 사용한다
 * 두번째 터미널에서 pkttyagent -- process pid
 * 이때, 두번째 터미널은 대기상태에 들어간다
 * 다시 첫번째 터미널에서 pkexec su
 * 두번째 터미널에서 비밀번호 입력창이 나오면 비밀번호를 입력한다
 * 인증에 실패해도 첫번째 터미널에서 sudoers에 접근할 수 있다
 * 수정하고 저장한다

#### 참고:
https://blog.naver.com/PostView.nhn?blogId=jgalgil&logNo=222264194082&parentCategoryNo=&categoryNo=30&viewDate=&isShowPopularPosts=true&from=search
