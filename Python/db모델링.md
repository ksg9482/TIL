### DB모델링 
어떤 item에 속성 데이터를 사전에 정의하는 것. 데이터 자체가 아니라 포맷을 지정하는것으로, 미리 지정해둔 포맷에 맞춰 저장하고 포맷에 해당하는 형식으로 데이터를 불러온다.
* 예: job table
  * id
  * 산업
  * 연봉
  * 근무지
  * 생성일
  * 수정일

### django의 경우
* id는 기본값(Primary Key)으로 자동 정의.
* 외래키(Foreign Key)는 xxx_id로 자동 생성
  * 다른 테이블의 id를 location으로 정의해주면 location_id 컬럼으로 생성.
* users 테이블은 자동으로 생성되어 있음.

### 마이그레이션 파일 생성 및 마이그레이트
* python manage.py makemigrations 모델에 해당하는 마이그레이션 생성.
* python manage.py migrate 생성한 마이그레이션으로 db에 테이블 생성.

### 유저 테이블에 수퍼유저 생성
* python manage.py createsuperuser 수퍼유저 생성.
* 생성한 수퍼유저로 장고 admin 페이지 접근 가능.
