# append()와 extend()와 insert()
배열을 다룰 때, 배열 내부에 값을 추가하기 위해 사용한다.
### append()
array.append(x)형태로 사용한다.   
값을 입력하면 배열 맨 끝에 객체로 추가하고, iterable 자료형이라도 객체로 저장한다.
```python
nums = [1,2]
nums.append(3)
[1,2,3]
```
```python
nums = [1,2]
nums.append([3,4])
[1,2,[3,4]]
```

### extend()
array.extend(<b>[iterable]</b>)형태로 사용한다. 
입력한 iterable 자료형을 배열의 끝에 각각 추가하고, 입력한 값이 iterable 자료형이 아닐경우 type error가 발생한다.
```python
nums = [1,2]
nums.extend([3,4])
[1,2,3,4]
```

### insert()
array.insert(i,x)형태로 사용한다. 원하는 위치 i 앞에 x를 추가 할 수 있다.   
i가 음수일 경우 배열의 끝을 기준으로 처리하고, 맨 끝에 추가하기 원하는 경우 insert(len(i), x)로 입력한다.   
추가할 값 x는 객체로 추가되며, iterable 자료형이라도 객체로 저장된다.
```python
nums = [1,2]
nums.insert(1, [3,4])
[1,[3,4],2]
```
