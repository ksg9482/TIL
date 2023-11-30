# Client와 Pool
PostgreSQL의 NodeJS 라이브러리인 pg에서는 DB커넥션을 설정하는 방법이 2가지 있다. 하나는 pool이고, 하나는 client이다.
node-postgres의 설명에 따르면 node-postgres는 libpq및 psql과 동일한 환경변수를 사용하여 PostgreSQL 서버에 연결한다고 한다. 개별 Client와 Pool 모두 이러한 환경 변수를 사용한다.

```javascript
const pool = new Pool({
  user: 'dbuser',
  host: 'database.server.com',
  database: 'mydb',
  password: 'secretpassword',
  port: 3211,
})

const client = new Client({
  user: 'dbuser',
  host: 'database.server.com',
  database: 'mydb',
  password: 'secretpassword',
  port: 3211,
})

// Pool과 Client 모두 동일한 환경변수 사용
```

그렇다면 왜 client와 pool로 나뉜걸까? 나눌만한 충분한 이유가 없다면 나누지 않았을 테니 충분한 이유가 있을 것이다.
client와 pool 하나씩 간단히 짚어보자. 

### Client와 Pool
#### Client
클라이언트는 PostgreSQL 서버에 접속하여 데이터를 주고 받는 역할을 한다. 

직접적으로 Client를 선언하여 PostgreSQL 서버에 접근할 수 있고, Pool을 이용할 때에도 pool.connect()을 통해 풀에서 유휴 클라이언트(풀 상황에 따라 작동방식이 다르다)를 획득한다.\

#### Pool
풀은 클라이언트의 집합이고 클라이언트들을 보다 효과적으로 관리하는 일종의 툴이다. 자주 쿼리하는 웹 어플리케이션이나 기타 소프트웨어에서 작업하는 경우 커넥션 풀을 이용하는 것이 권장된다.

node-postgres를 이용하는 가장 쉽고 일반적인 방법으로 소개하는 것도 pool을 이용하는 것이다.(pool.query())

#### 왜 Pool을 권장하는가?
* 새 클라이언트를 PostgreSQL 서버에 연결시 20~30밀리초 정도 핸드셰이크가 필요하다.
* PostgreSQL 서버는 한 번에 제한된 수의 클라이언트만 처리할 수 있다. (참고: https://wiki.postgresql.org/wiki/Number_Of_Database_Connections)
* PostgreSQL은 연결된 단일 클라이언트에서 선입선출 방식으로 한번에 하나의 쿼리만 처리 할 수 있다. 만약 단일 클라이언트로만 사용하는 경우 모든 동시 요청은 순차적으로 파이프라인 된다.

#### Pool은 언제나 정답인가?
일반적인 접근법으로는 연결이 빈번하거나 동시 요청이 많은 경우 Pool을 이용하고, 
단일 트랜잭션만 사용하여 런타임 동안 최대 하나의 열린 연결을 갖는 스크립트나 도구를 작성하는 경우 단일 Client 이용한다.

Pool을 통해 PostgreSQL 서버에 접근할 때 가장 주의해야 하는 부분도 트랜잭션이다.

트랜잭션 내의 모든 질의문은 동일한 클라이언트 인스턴스를 사용해야 한다. pool을 이용한다면 동일한 client 제공을 보장할 수 없다.
pool.query로 사용할 경우 유휴 클라이언트부터 이용하고 연속적으로 쿼리하면 각 클라이언트들이 별도로 받기 때문이다. 

트랜잭션 처리를 위해 독립된 클라이언트를 확보하려면 pool.connect()을 통해 풀에서 클라이언트를 획득해야 한다.

### pool에서 트랜잭션 사용하기
트랜잭션을 실행하려면 클라이언트를 통해 BEGIN / COMMIT / ROLLBACK를 통해 직접 쿼리를 실행하면 된다. 

```javascript
const pool = new Pool()
const client = await pool.connect()

try {
  await client.query('BEGIN') //트랜잭션 선언
  const queryText = 'INSERT INTO users(name) VALUES($1) RETURNING id' //격리해야 하는 작업 실행
  const res = await client.query(queryText, ['brianc'])
 
  const insertPhotoText = 'INSERT INTO photos(user_id, photo_url) VALUES ($1, $2)'
  const insertPhotoValues = [res.rows[0].id, 's3.bucket.foo']
  await client.query(insertPhotoText, insertPhotoValues)
  await client.query('COMMIT') //커밋
} catch (e) {
  await client.query('ROLLBACK') //실패시 롤백
  throw e
} finally {
  client.release() //항상 클라이언트를 되돌려줘야 한다.
}
```

### 요약
연결이 빈번하고 동시 요청이 많은 웹 어플리케이션에서는 Pool을 이용해 커넥션을 관리한다. 트랜잭션 처리를 할 때에는 주의가 필요한데, pool.connect()을 통해 풀에서 클라이언트를 획득하여 동일 클라이언트를 이용해야 한다.
그리고 풀에서 클라이언트를 명시적으로 획득했다면 client.release()를 통해 명시적으로 클라이언트 반환을 해주어야 한다.

####참조
[https://stackoverflow.com/questions/48751505/how-can-i-choose-between-client-or-pool-for-node-postgres](https://stackoverflow.com/questions/48751505/how-can-i-choose-between-client-or-pool-for-node-postgres)
[https://node-postgres.com/features/pooling](https://node-postgres.com/features/pooling)
