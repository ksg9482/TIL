# Array
### 배열이란?
일반적으로 배열이란 동일한 크기의 메모리 공간이 빈틈없이 나열된 지료구조를 말한다.   
즉, 배열의 요소는 하나의 타입으로 통일되어 있으며 서로 연속적으로 인접해있다. 이를 밀집배열(dense array)이라 한다.   
배열의 요소는 동일한 크기로 갖고 연속적으로 이어져 있으므로 인덱스를 통해 단 한번의 연산으로 임의의 요소에 접근 할 수 있다.   
이를 임의 접근random access이라 하고, 시간복잡도 O(1)을 갖는다.배열은 효율적이고 고속이다.   

* \[검색대상 요소의 메모리 주소: 배열의 시작 메모리 주소 + 인덱스 * 요소의 바이트 수\]
* \[인덱스가 0인 요소의 메모리 주소: 1000 + 0 * 8 = 1000\]
* \[인덱스가 1인 요소의 메모리 주소: 1000 + 1 * 8 = 1008\]

하지만 정렬되지 않은 배열에서 특정 값을 탐색하는 경우 처음부터 탐색(선형 탐색linear search, O(n))해야 하고,   
배열에 요소를 삽입하거나 삭제하는 경우 배열 요소를 연속적으로 유지하기 위해 요소를 이동시켜야 한다.

#### 선형탐색
```javascript
function linearSearch(array, target) {
	const length = array.length;

	for (let i = 0; i < length; i++;) {
		if(array[i] === target) return i
	}

	return -1
}
```
### 자바스크립트의 배열
자바스크립트의 배열은 일반적인 배열과 다르다. 배열의 요소를 위한 메모리 공간은 동일한 크기를 갖지 않아도 되고 연속적이지 않을 수 있다.   
이처럼 배열의 요소가 연속적으로 이어져 있지 않은 배열을 희소배열(sparse array)이라 한다.   
사실, 자바스크립트의 배열은 일반적인 배열의 동작을 흉내낸 특수한 객체이다.   
   
```javascript
const arr = ['string', 1, true, null, undefined, [], {}, function() {}];
console.log(Object.getOwnPropertyDescriptors(arr));

/*{
  0: {value: 'string', writable: true, enumerable: true, configurable: true}
  1: {value: 1, writable: true, enumerable: true, configurable: true}
  2: {value: true, writable: true, enumerable: true, configurable: true}
  3: {value: null, writable: true, enumerable: true, configurable: true}
  4: {value: undefined, writable: true, enumerable: true, configurable: true}
  5: {value: Array(0), writable: true, enumerable: true, configurable: true}
  6: {value: {…}, writable: true, enumerable: true, configurable: true}
  7: {writable: true, enumerable: true, configurable: true, value: ƒ}
  length: {value: 8, writable: true, enumerable: false, configurable: false}
}*/
```
자바스크립트 배열은 인덱스를 프로퍼티 키로 갖고 있으며 length 프로퍼티를 갖는 특수한 객체이다.   
즉, 모든 값은 객체의 프로퍼티 값이 될 수 있으므로 어떤 타입의 값도 배열의 요소가 될 수 있다.   
   
자바스크립트 배열은 일반적인 배열보다 접근이 느리지만 특정 요소를 탐색, 삽입, 삭제하는 경우에 빠르다.   
자바스크립트 엔진은 '자바스크립트의 배열'이 가지는 구조적 단점을 보완하기 위해 일반 객체와 구별해 최적화 했고,   
배열과 일반 객체의 성능을 테스트 해보면 배열이 일반 객체보다 빠르다.

```javascript
const arr = [];
console.time('Array Performance Test');
for (let i = 0; i < 10000000; i++) {
  arr[i] = i;
}
console.timeEnd('Array Performance Test');

const obj = {};
console.time('Object Performance Test');
for (let i = 0; i < 10000000; i++) {
  obj[i] = i;
}
console.timeEnd('Object Performance Test');
/*
Array Performance Test: 123.580810546875 ms
Object Performance Test: 207.60986328125 ms

Array Performance Test: 145.924072265625 ms
Object Performance Test: 205.825927734375 ms

Array Performance Test: 164.761962890625 ms
Object Performance Test: 223.06201171875 ms
*/
```
