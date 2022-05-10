### Error: posts.belongsTo called with something that's not a subclass of Sequelize.Model
#### 내용: posts.belongsTo가 Sequelize.Model의 하위 클래스가 아닌 것으로 호출되었다.
* 원인: 관계형으로 묶어서 외래키를 적용하려 했는데, 테이블을 생성하지 않은 채 묶으려해서 발생했다.
  * 해결: 각 테이블을 만들때 관계성 처리도 한꺼번에 하려고 해서 발생한 문제다. 테이블의 생성 순서를 조정해서 관계성 설정에 필요한 테이블이 미리 구성되도록 했다.
  * 앞으로: 관계성을 설정할 때 외래키를 적용할 테이블에서 필요한 관계성도 다루게 했다.
이전엔 각 테이블 생성파일에 관계성을 테이블 이름에 맞춰 흩어두었다면, 이후는 외래키를 적용하는 테이블에서 관계성을 어떻게 맺을 것인지 모아둔다.

#### 이전
```javascript
//Users table
Users.init(...)
Users.hasMany(Posts)

//Posts table
Posts.init(...)
Posts.belongsTo(Users)
```

#### 이후
```javascript
//Users table
Users.init(...)

//Posts table
Posts.init(...)
Users.hasMany(Posts)
Posts.belongsTo(Users)
```
