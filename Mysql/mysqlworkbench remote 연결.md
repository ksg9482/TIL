# mysqlworkbench remote 연결

### 발단
wsl 내부에 있는 mysql을 windows mysql workbench에 연결하려고 했다.   
ifconfig로 IPv4 address를 찾아서 mysql workbench에 연결했으나 바로 오류 발생했다.   
알아보니 user에게 remote 연결 권한을 주어야 한다고 한다.

### 과정
/etc/mysql/mysql.conf.d에 있는 mysqld.cnf파일을 nano로 편집, bind-address를 127.0.0.1 -> 0.0.0.0로 변경한다.   
 * 127.0.0.1이면 127.0.0.1:port만 접근할 수 있지만, 0.0.0.0이면 모든 접속을 허용한다. 즉 remote 접속이 가능하다.
   * 실제로 sudo netstat -ntlp | grep mysqld로 확인해보면 0.0.0.0:3306으로 설정되어 있다. 
   * 만약 mysql을 실행하고 있었다면 restart해야 한다.
 * GRANT ALL PRIVILEGES ON \*.\* TO 'root'@'%';
   * root 사용자에게 모든 데이터베이스, 테이블에 대한 권한을 주고, 리모트 접속을 허용한다.
   * \*.\* - 모든 데이터베이스와 모든 테이블.
   * "%" - localhost가 아니라 외부 접속도 허용.
   * 하지만 조심해서 써야한다. root 사용자에게 권한을 주는 건 보안상 좋지 않다. 
   * GRANT ALL PRIVILEGES ON \*.\* TO 'root'@'%' IDENTIFIED BY '비밀번호'; 를 쓴다는 경우도 있는데   
    MySQL version 5.7.6. 이후엔 GRANT 문과 함께 IDENTIFIED BY를 쓰지 않는다.
 * FLUSH PRIVILEGES;
   * 권한 적용. 이것까지 해야 권한이 적용된다.

### 에러 핸들링
맨처음에 GRANT ALL PRIVILEGES ON \*.\* TO 'root'@'%';로 권한을 부여햐려 했더니 오류가 발생했다.
 * 'root'@'%' user가 없기 때문이다. 'root'@'%'와 'root'@'localhost'는 다르다.
 * <create user 'root'@'%' identified by '비밀번호';> 로 'root'@'%' user를 생성해주어야 한다. 
   *  생성 후 <SELECT User, Host FROM mysql.user;> 로 확인해보면 host가 '%', 'localhost' 별도로 만들어져 있다.
 ___

유저를 생성하려고 했으나 비밀번호 제약조건에 맞지 않아서 확인했다.
<Your password does not satisfy the current policy requirements>
     
 * SHOW VARIABLES LIKE 'validate_password%'; 로 제약조건 확인.
   
결과:
validate_password.check_user_name: ON - 비밀번호에 user name이 들어가면 안된다.   
validate_password.dictionary_file:    
validate_password.length: 8 - 비밀번호 최소 길이는 8이다.    
validate_password.mixed_case_count: 1 - 비밀번호에 대소문자가 1번은 섞여야 한다.   
validate_password.number_count: 1 - 비밀번호에 숫자가 1번은 쓰여야 한다.      
validate_password.policy: MEDIUM - 설정을 변경하려면 LOW여야 한다.     
validate_password.special_char_count: 1 - 비밀번호에 특수문자가 1번은 쓰여야 한다.   

* 조건에 맞춰서 비밀번호를 설정하여 'root'@'%' 유저를 생성했다.  

  


