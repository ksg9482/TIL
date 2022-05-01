```javascript
curl -v http://example.com -l -H "origin: https://origin.example.com/"
```
### 옵션
 * -v: 상세로그 보기
 * -l: 지정한 리소스의 http헤더만 가져온다
 * -H: header추가. "origin: xxx"를 입력하면 헤더에 "origin: xxx"가 추가된다

curl을 이용하면 cors에러가 있을때 도메인이 origin을 보내주는지 확인할 수 있다
