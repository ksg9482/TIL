# 해시와 맵

### 해시
해시(hash)란 데이터의 효율적인 관리를 목적으로 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 자료구조이다. 쉽게 말하자면 key-value로 데이터를 관리하는 것이다.
### 맵
Map:  Map, Set은 ES6에서 새로 도입한 자료구조다. Map 객체는 키-값을 저장하는데 키는 자료형을 구분한다. 그리고 new Map을 만들때 배열을 넣어서 초기값을 지정 할 수 있다.

**언제 필요한가?**

- 문자열, 심볼 말고 key값으로 설정할 경우(map, set은 1과 '1'을 구분한다)
- 객체의 프로퍼티 개수를 알아야 할 경우(size)
- for of 또는 spread 문법을 적용할 경우(일반적인 객체는 not iterable이다. map은 iterable해서 for of, forEach로 접근할 수 있다.)

**has(Map.prototype.has())**: Map객체에 해당하는 키가 있는지 확인한다.

```jsx
const map1 = new Map();
map1.set('bar', 'foo');

console.log(map1.has('bar'));
// expected output: true

console.log(map1.has('baz'));
// expected output: false
```

**set(Map.prototype.set()):** Map객체에 해당하는 키-값 한 쌍을 추가하거나 업데이트 한다.

```jsx
const map1 = new Map();
map1.set('bar', 'foo');

console.log(map1.get('bar'));
// expected output: "foo"

console.log(map1.get('baz'));
// expected output: undefined
```

**get(Map.prototype.get()):** Map객체에서 지정된 요소를 반환한다. 연결된 값이 객체인 경우 해당 객체에 대한 참조를 얻게 되며, 해당 객체에 대한 모든 변경 사항은 객체 내부에 적용된다.

```jsx
const map1 = new Map();
map1.set('bar', 'foo');

console.log(map1.get('bar'));
// expected output: "foo"

console.log(map1.get('baz'));
// expected output: undefined
```

**value(Map.prototype.value()):** Map객체에 삽입된 순서로 각 요소에 대한 값을 포함하는 새 iterable 개체를 반환한다.

```jsx
const myMap = new Map();
myMap.set('0', 'foo');
myMap.set(1, 'bar');
myMap.set({}, 'baz');

const mapIter = myMap.values();

console.log(mapIter.next().value); // "foo"
console.log(mapIter.next().value); // "bar"
console.log(mapIter.next().value); // "baz"
```
