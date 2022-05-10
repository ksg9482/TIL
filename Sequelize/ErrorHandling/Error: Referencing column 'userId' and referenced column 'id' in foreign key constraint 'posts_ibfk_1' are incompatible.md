### Error: Referencing column 'userId' and referenced column 'id' in foreign key constraint 'posts_ibfk_1' are incompatible.
#### 내용: Users table의 id를 posts table의 userId에 외래키로 관계성을 설정하려고 하는데 'id'와 'userId'는 서로 호환되지 않는다.
* 원인:  Users table의 id는 BIGINT였는데 posts table의 userId는 INTEGER로 설정해 놓았다. 
  * 해결: id와 외래키 적용하는 모든 타입을 INTEGER로 변경했다. (BIGINT로 하기에는 낭비라고 판단했다.)
  * 앞으로: 다른 table의 외래키가 들어갈 부분을 제대로 통일한다. 애초에 데이터베이스를 설계할 때 어디를 BIGINT로 할지 INTEGER로 할지 확실히 구분을 해야겠다.
