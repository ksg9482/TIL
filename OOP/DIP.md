# DIP

### 고수준 모듈과 저수준 모듈
* 고수준 모듈
  * 의미 있는 단일 기능 제공
  * 상위 수준의 정책 구현

* 저수준 모듈
  * 고수준 모듈을 구현하기 위해 필요한 하위 기능의 실제 구현

고수준 모듈은 기능의 정책을 제공하고 저수준 모듈은 하위 기능의 구현을 제공한다.

### 고수준이 저수준에 직접 의존하면?
저수준 모듈이 변경되면 고수준 정책이 바뀌지 않았음에도 고수준 모듈을 변경해야 한다.

고수준 모듈이 저수준 모듈에 의존하면서 발생하는 문제를 해결하기 위한 원칙이 의존 역전 원칙(DIP, Dependency Inversion Principle)이다.

### 의존 역전 원칙(DIP)
* 고수준 모듈은 저수준 모듈의 구현에 의존하면 안된다.
* 저수준 모듈이 고수준 모듈에서 정의한 추상타입에 의존해야 한다.

### 고수준 관점에서 추상화
DIP에서 하위 기능에 대한 추상타입을 도출할 때에는 고수준 입장에서 추상화해야 한다.
```
예: 요구사항 - 예외가 발생할 경우 Sentry로 예외를 수집한다.
SentryClientService를 구현해 예외 데이터를 전송하도록 로직 작성. 
```
* 이 때, 저수준 관점에서 추상화하면 Sentry가 중심이 되고, SentryService라는 타입이 도출된다.
* 반면 고수준 관점에서 예외를 수집한다는 하위 기능을 추상화 한다면 예외 수집 즉, ExceptionCollector를 도출할 수 있다.
* 같은 추상타입이지만 SentryService는 저수준 모듈의 구현에 가깝고 ExceptionCollector는 고수준 모듈의 정책에 더 가깝다.

DIP를 적용하면 고수준 모듈을 변경하지 않으면서 저수준 모듈을 변경할 수 있는 유연함이 생긴다. 
만약 예외 수집을 Sentry가 아니라 다른 서비스를 통해 수집하는 것으로 요구사항이 변경되어도 고수준 모듈은 변함 없고 저수준 모듈만 알맞게 구현하면 된다.

### DIP를 잘 따르는 구조
처음부터 좋은 설계가 바로 나오지 않는다. 부단한 추상화 노력이 필요하고, 요구사항과 업무 이해가 높아지면서 고수준 관점에서 저수준 모듈을 인지하고 저수준 모듈에 대한 추상화를 시도하게 된다.

예를 들어 예외 수집의 경우에도 핵심은 Sentry에 예외를 보낸다가 아니라, 예외를 수집한다는 기능이 핵심이고 Sentry는 변경이 가능한 사항이라는 것을 알 수 있다.

### 결론
DIP만 잘해도 좋은 설계가 될 가능성이 높아진다. 중요한 건 고수준에서 도출한 추상화를 저수준 모듈이 따라야 한다는 것이다.
