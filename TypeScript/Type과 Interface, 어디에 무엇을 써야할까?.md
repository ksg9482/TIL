# Type과 Interface, 어디에 무엇을 써야할까?

### 타입
리터럴 타입에서만 사용.   
```javascript
type someType = 'one' | 'two' | 'three';
```
   
### 인터페이스
Object 형태의 타입은 인터페이스 사용.   
```javascript
interface IsomeInterface {
  name: string;
  age: number;
};
```

### 알아둘 사항
* typescript 3.x 부터 인터페이스 앞에 대문자 I를 강제하게 되었다.
  * 해당 옵션은 끌 수 있다.
* 타입에는 대문자 T를 강제하지는 않는다.
* 타입은 enum으로 대체하는 경우도 있다.
