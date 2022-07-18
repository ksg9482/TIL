# ECMAScript 모듈
ES 또는 ESM으로 알려진 ECMAScript 2015명세의 일부분으로 JavaScript에 서로 다른 실행 환경에서도 적합한 공식 모듈 시스템을 부여하기 위해 도입되었다. ESM과 CommonJS 사이의 가장 큰 차이점은 ESM은 static이라는 것이다. 즉, import가 모든 모듈의 가장 상위 레벨과 제어 흐름 구문의 바깥쪽에 기술된다. import 할 때 모듈의 이름을 코드를 이용하여 동적으로 생성 할 수 없고, 상수 문자열만이 허용된다.
* 정적 import는 사용하지 않는 코드 제거 등 코드 최적화를 해줄 수 있는 종속성 트리의 정적 분석을 가능하게 해준다.
* Node.js는 모든 .js 파일이 CommonJS를 사용한다고 인식하기 때문에 package.json의 "type" 필드에 "module"을 기재한다.
* CommonJS는 export와 module.export를 사용하지만, ESM는 export만 사용한다.
* ESM은 기본적으로 모든것이 private이기 때문에 export된 개체들만 다른 모듈에서 접근 가능하다.
* import 키워드(ESM)를 쓸 때는 CommonJS와는 다르게 확장자를 구체적으로 명시해야 한다.
* ESM은 암시적으로 strict mode에서 실행된다. 
  * strict mode이기 때문에, require, export, module, exports, __filename, __dirname 등 몇가지 참조가 정의되지 않는다.
  * ESM에서는 특별한 객체인 import.meta를 사용하여 현재 파일에 대한 참조를 얻을 수 있고, 이 값으로 절대 경로 형식에 대한 __filename과 __dirname을 재구성하는데 사용 할 수 있다.
* ESM의 경우 전역범위에서 this는 undefined인 반면, CommonJS의 경우는 this가 exports와 같은 참조를 한다.
  * console.log(this === exports)  

## export와 export default
CommonJS에서는 이름 없는 하나의 개체를 module.exports에 할당하여 익스포트 할 수 있다. 이는 모듈 개발자에게 단일 책임 원칙을 권장하고 깔끔한 하나의 인터페이스를 노출 한다.
ESM에서도 비슷한 동작을 할 수 있는데, 이를 default export라고 부르고 익스포트 되는 개체는 default라는 이름 아래 등록된다.

default export는 이름이 없는 것으로 간주되기 때문에 이름을 명시한 ESM의 import와는 다르다. 임포트와 동시에 지정한 이름으로 할당 된다. 내부적으로는 default export는 default라는 이름으로 익스포트 되는 것과 동일하다.
* default 개체를 명시적으로 임포트 할 수는 없다. ( import { default } from './someModule.js' (X) )
* default는 객체의 속성으로서는 유효하지만, 스코프 내에서 default라는 이름의 변수를 직접 사용할 수는 없다.


#### export 
* 이름을 명확히 지정한다. 지정된 이름을 갖는다는 것은 IDE로 자동완성, 자동 임포트등 개발자에게 도움을 줄 수 있게 만든다.

#### export default
* 주어진 기능이 서로 다른 파일에서 서로 다른이름을 가질 수 있게한다. 따라서 주어진 이름에 어떤 모듈이 적용될 것인지 추록하기 힘들어진다.
* 모듈에서 가장 핵심적인 한가지 기능과 연결하기에 편리하다. 사용자 관점에서 봤을 때, 바인딩을 위한 정확한 이름을 알 필요가 없이 기능의 확실한 부분을 임포트 할 수 있게 해준다.
* 그러나 특정상황에서, 사용하지 않는 코드의 제거 작업을 힘들게 만든다.


따라서 명확하게 하나의 기능을 익스포트 하고 싶을 때에는 export default를 사용하되, 이름을 사용한 export 사용에 습관을 들이는 것이 일반적으로 좋은 방법이다. 특히 하나 이상의 기능을 내보내고 싶을 때에는 특히 그렇다.


## 모듈 식별자
모듈 식별자는 import 구문에서 적재하고 싶은 모듈의 경로는 명시할 때 쓰이는 값이다.
* 상대적 식별자(Relative) - ./someModule.js 또는 ../../someModule.js 와 같이 임포트하는 파일의 경로에 상대적 경로가 사용된다.
* 절대적 식별자(Absolute) - file:///opt/nodejs/config.js 와 같이 직접적이고 완전한 경호가 사용된다.
  * ESM에서만 사용 가능하고 / 또는 //가 선행 했을 경우 동작하지 않는다.
* 노출 식별자(Bare) - http 등 node_modules 폴더에서 사용 가능하고 패키지 매니저를 통해 설치된 모듈 또는 Node.js 코어 모듈을 가리킨다.
* 심층 임포트 식별자(Deep import) - someNodeModule/lib/someModule.js 와 같이 node_module에 있는 패키지의 경로를 가리킨다.
* 브라우저 환경에서는 모듈의 URL을 명시하여 직접 임포트 할 수 있지만 Node.js에서는 지원되지 않는다.


## 비동기 임포트
import 구문은 정적이기에 모듈 식별자가 실행 중에 생성될 수 없고, 제어 구문 내에 포함 될 수 없다. 이런 제약을 극복하기 위해 ESM은 비동기 임포트(동적 임포트)를 제공한다.
import()연산자를 사용하는데, import()연산자는 문법적으로 모듈 식별자를 인자로 취하고 모듈 객체를 프라미스로 난환하는 함수와 동일하다.

* 모듈의 이름을 동적으로 생성한다
* 모듈을 동적으로 임포트 하기 위해 import()를 사용한다.
* 동적 임포트는 비동기적으로 작동하기 때문에, .then()을 반환된 프라미스에 사용한다.
* 모듈이 완전히 적재되면 then으로 전달된 함수가 작동한다.
```javascript
// wellcome-en.js
export const HELLO = 'hello'

// wellcome-ko.js
export const HELLO - '안녕하세요'

// main.js
// selectLanguage 로직 생략. en 또는 ko이 선택됨
const wellcomeModule = `./wellcome-${selectLanguage}`
import( wellcomeModule )
	.then(( wellcomeString ) => {
		// wellcomeString은 동적 임포트된 모듈의 네임스페이스가 된다.
		console.log(wellcomeString.HELLO)
})
)
```
