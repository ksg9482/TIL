### private 접근제어자
타입 스크립트는 private 접근제어자를 이용한다. 하지만 자바스크립트에서 지원하는 방식이 아니다보니 TS -> JS 컴파일을 거치면 접근제어자는 사라진다.

결국 private _property 방식으로 언더스코어(_)를 이용하여 접근할 수 없음을 표현했다. 이 방법도 마찬가지로 접근을 차단할 수는 없다.

### ECMA2022
ECMA2022에서 #키워드가 추가되었다. #property 방식으로 속성 앞에 #을 붙이면 된다. 

언더스코어 방식과 달리 정말로 접근할 수 없고, 멤버 여부를 알아보려면 전용 메서드를 사용해야 한다.

타입스크립트에서만 사용할 수 있었던 private와는 다르게 TS -> JS 컴파일을 거쳐도 접근제어자로서의 역할을 수행한다.

단, private #property 방식으로는 쓸 수 없다. 접근 제어자를 사용하지 말고 그대로 쓰면 된다.
클래스 내부에서도 이용방법은 같다. this.#property 방식.
