# Error Handle
### Jest has detected the following 1 open handle potentially keeping Jest from exitingd 에러
* <b>원인:</b> express 또는 비동기 node app은 jest 실행이 완료되어도 비동기가 남아있는 경우 jest가 종료되지 않는다.   
종료되지 않은 비동기가 있어 에러가 발생한 것.
* <b>해결:</b> npm run test 부분에 --forceExit 옵션을 적용한다. 이는 테스트가 끝나면 강제 종료하라는 뜻이다.
