# SQL문_DDL
DDL은 데이터 정의 언어로 데이터를 담고 있는 구조와 연결되어 있다.   
   
### 데이터를 담는 구조(Database Object)의 5가지 종류
* table: 데이터를 저장하는 기본 저장 단위. 행과 열로 구성.
* view: 테이블을 바라보는 쿼리문이 출력되는 결과(하나 이상의 테이블에 있는 데이터의 부분집합)
* sequence: 일련번호 생성기(번호를 생성하는 DB오브젝트)
* synonym: 테이블에 또다른 이름을 부여
* index: 검색 속도를 향상시키기 위한 DB오브젝트
   
### DDL 명령어
* create: 데이터를 저장하는 가장 기본 저장 단위인 table을 생성한다.
* alter: 테이블의 특정 컬럼을 삭제, 추가, 변경한다.
* drop, truncate: 데이터를 삭제한다. delete와의 차이점은 rollback, flashback의 가능 여부다. 
  * delete는 rollback, flashback이 가능하지만 drop, truncate는 불가능하다.(drop일 경우 flashback은 가능하다)
* rename: 오브젝트의 이름을 변경하는 명령어로, 이름을 변경할 객체가 있어야 한다.
