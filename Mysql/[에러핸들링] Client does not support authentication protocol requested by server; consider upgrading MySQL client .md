### 개요
NodeJS로 MySQL에 연결해서 데이터를 입력하려고 했다. MySQL는 이미 몇번이고 이용한 관계로 연결 과정에서 에러가 날 것이라고는 예상도 못했다.

### 에러
Client does not support authentication protocol requested by server; consider upgrading MySQL client

클라이언트가 서버에서 요청한 인증 프로토콜을 소화할 수 없다고 한다. MySQL을 업그레이드 하라는 권유는 덤이다.

### 원인
password plugin이 원인이다.

caching_sha2_password을 소화하지 못해서 발생하는데, mysql_native_password로 plugin을 변경하면 된다.

```
ALTER USER <USER>@<HOST> IDENTIFIED WITH mysql_native_password BY <PASSWORD>;
```

* <USER>: DB User에 등록된 사용자명. root사용자면 root이다.
* <HOST>: DB User에 등록된 호스트. 보통 localhost 또는 %(와일드카드)이다. %는 모든 호스트에 해당한다.
* <PASSWORD>: DB User에 등록된 비밀번호. 암호화 로직을 재설정하여 비밀번호를 저장하기 때문에 비밀번호도 입력해야 한다. plugin이 바뀌면 동일 비밀번호를 입력해도 암호화된 결과물이 달라지는 것을 확인할 수 있다.

### caching_sha2_password
MySql 8.0은 SHA-256 hashing을 구현하는 두 가지 인증 플러그인을 지원한다.
* 기본적인 SHA-256 인증을 구현한 sha256_password 플러그인
* sha256_password와 동일한데 성능 향샹을 위해 서버 캐싱을 이용하는 caching_sha2_password 플러그인

문제는 caching_sha2_password를 사용하려면 SSL 보안연결을 사용하거나 RSA 보안을 적용한 비암호 연결을 사용해야 하는 등 제약사항이 생긴다.

그래서 구식인 mysql_native_password을 사용하는 것으로 caching_sha2_password에 관한 문제를 피할 수 있다.

하지만 에러 로그에서 'consider upgrading MySQL client'라고 안내하는 만큼 우선 업데이트 부터 시도하는 게 장기적으로 좋을 것 같다.
