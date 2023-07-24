### 에러 메시지
MySQL Error 1093 : You can't specify target table 'tablename' for update in FROM clause

### 에러 원인
MySQL은 자기 테이블의 데이터를 바로 사용 못하므로 자기 테이블의 데이터를 읽는 SQL을 실행시 1093 에러가 발생함.

### 에러 해결
Sub Query를 하나 더 넣고 sub query 결과를 임시 테이블로 만든후에 실행하면 해결된다.

### 쿼리
해당 쿼리는 Column1의 값 +1, Column2를 삽입하는 쿼리. COUNT가 아니라 MAX로 가장 큰 값에 +1 해도 된다.
```sql
INSERT INTO `Table Name`(Column1,Column2)
VALUES(
  (SELECT COUNT(tmp.Column1)+1
   FROM (
       SELECT Column1 FROM `Table Name`
   )tmp)
  ,Value2
);
```
