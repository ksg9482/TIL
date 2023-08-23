# Mysql DB 또는 테이블 가져오기, 내보내기.md

### 내보내기 mysqldump
mysql에 접속해서 실행하는 것이 아니라 터미널에서 mysqldump 커맨드를 실행한다.
* DB의 모든 테이블 내보내기
  * mysqldump -u <mysql 유저 아이디> -p <DB명> > <저장할 이름>.sql
* DB의 특정 테이블 내보내기
  * mysqldump -u <mysql 유저 아이디> -p <DB명> <테이블명> > <저장할 이름>.sql
 
### 가져오기 source
mysql에 접속한 상태에서 실행한다.
* sql파일을 기반으로 테이블 및 내용을 생성한다
  *  source <파일경로/sql파일명>
