# pipe기법
파이프는 단방향 통신을 위한 용도로 사용된다. 하나의 파이프는 이전 파이프에서 전달된 결과를 파라미터로 삼아 또 다른 결과를 반환한다.
파이프가 반환하는 값은 그 다음 파이프의 입력값으로 전달된다. 따라서 순수함수를 이용하여 상황에 따라 변하지 않아야 한다.
순수함수는 같은 입력값일 때 같은 반환값을 보장한다. 또, 함수 외부 scope값을 바꾸지 않는다.

### 전개
1. reduce에 포함시키고 싶은 모든 함수를 넣을 수 있게 한다.
2. 함수 내부를 채운다.
3. 초기값 설정
4. 일반화
5. 클로져 이용

### pipe를 사용하지 않은 경우
```javascript
const addFour = a => a + 4;
const minusFive = a => a - 5;
const multiplyByTen = a => a * 10;

const nine = addFour(5);
const four = minusFive(nine);

addFour(minusFive(0)); // -1
multiplyByTen(addFour(minusFive(0))); // -10
Math.abs(multiplyByTen(addFour(minusFive(0)))); // 10
```

### pipe함수를 만들어 순차적으로 실행할 경우
```javascript
//1. reduce에 포함시키고 싶은 모든 함수를 넣을 수 있게 한다.
  const pipe = (funcs) => {
    return funcs.reduce((res, func) => {
        //acc 는 반환될 값, cur 는 원본 배열에서 현재 참조하고 있는 값
        //acc -> res 반환값, cur -> func 현재 적용되는 함수
        //func.reduce는 다음 함수가 필요로하는 인자를 받을 수 있게 적절한 값을 반환해야 한다
    })
}
```

```javascript
//2. 함수 내부를 채운다
  const pipe = (funcs) => {
    return funcs.reduce((res, func) => {
        //누진된 res값을 적용시킬 함수에 인자로 입력한다. 
        //reduce는 그 반환값을 res에 적용하고 다음 함수에도 마찬가지로 동작한다.
        //하지만 처음 동작할 때는 초기값이 없기 때문에 첫번째 함수가 초기값으로 이용된다.
        //따라서 첫번째 함수도 제대로 동작할 수 있게끔 초기값을 적용해 주어야 한다.
        return func(res)
    })
}
```

```javascript
//3. 초기값 설정
  const pipe = (funcs, v) => {
    //함수들과 초기값(v:value)을 입력하면 함수들과 초기값이 reduce에 적용된다.
    //그러나 파이프는 배열밖에 받을 수 없으니 단일함수는 사용할 수 없다.
    return funcs.reduce((res, func) => { 
      return func(res)
    }, v)
}
```

```javascript
//4. 일반화
  const pipe = (v, ...funcs) => {
    //파이프가 단일 함수도 사용할 수 있도록 rest파라미터를 사용한다.
    //rest 파라미터는 마지막 순서에 적어야 하므로 함수와 값의 전달 위치를 변경한다.
    return funcs.reduce((res, func) => {
      return func(res)
    }, v)
}
```

```javascript
//5. 클로져 이용
  const pipe = (...funcs) => v => {
    //클로져는 이미 실행이 종료된 외부 함수의 프로퍼티는 참조할 수 있는 내부 함수를 뜻한다.
    //파이프는 v라는 값을 받는 또 다른 함수를 반환하는 형태가 되었다.
    //새롭게 반환된 함수가 v를 받을 때까지 파이프는 reduce를 실행하지 않는다.
    //클로져가 적용된 함수는 pipe(add)(5) 와 같이 호출한다.
    return funcs.reduce((res, func) => {
      return func(res)
    }, v)
}
```



[출처](https://medium.com/%EC%98%A4%EB%8A%98%EC%9D%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-pipe-c80dc7b389de)

