# any와 unknown
typescript는 자바스크립트에 타입을 도입하여 타입 오류로 인해 일어날만한 오류들은 사전에 방지해준다.   
하지만 지나치게 경직된 타입은 생산성을 떨어뜨리기도 하고 자바스크립트 모듈을 그대로 사용하기 어렵게도 한다.   

## any
타입스크립트에는 any라는 타입이 있는데, any타입은 잘 사용하면 타입스크립트의 생산성을 향상시켜준다.   
동시에 가장 문제가 되는 타입이기도 하다. any는 항상 타입검사를 만족시킴으로 타입을 검사하여 사전에 문제가 될 만한 부분을 검출한다는 타입스크립트의 강점을 퇴색시킨다.   
어떤 비정상적인 연산도 any 타입을 사용하면 타입검사로 걸러낼 수 없다.   

때문에 항상 any타입은 조심해서 사용해야 한다.   

## unknown
typescript 3.0에서 unknown타입이 도입되었는데, 이 타입은 any타입과 같이 모든 값을 허용하지만, 할당된 값이 어떤 타입인지 모르기 때문에 함부로 연산을 할 수 없다.   
unknown타입으로 변수를 정의하면 컴파일러는 어떤 값이든 올 수 있으니 더 엄격히 검사한다. 이 경우 조건문을 사용하여 타입 검사를 하면 동작하게 된다.   

any와 unknown 둘 다 타입스크립트의 코드를 유연하게 하는데 유용하지만, 보다 안전하게 타입을 이용하려면 unknown 타입을 사용하는 것이 좋다.
