### nestjs가 클래스 기반 주입을 사용하는 이유

왜 nestjs는 클래스 기반 주입을 사용하는가?

종속성 주입은 일반적으로 인터페이스를 기반으로 한다. 하지만 타입스크립트에서 인터페이스는 컴파일 시간에만 사용할 수 있다.

자바스크립트로 컴파일 된 이후는 신뢰 할 수 없으므로 클래스 기반 주입을 사용한다.
