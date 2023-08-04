# node.js에서 터미널 명령어를 사용하는 법
node.js의 빌트인 모듈인 child_process를 이용한다. child_process를 이용하는 방법은 크게 두가지가 있는데 spawn()과 exec()이다.   
둘 다 비슷한 역할을 하지만 작동방식에 차이가 존재한다. spawn()은 stream로 작동하고 exec은 buffer를 작동한다는 점이다.   
spawn()은 stdin, stdout, stderr을 통해 이용한다.
* stdin: 부모 프로세스로부터 자식 프로세스에게 데이터를 보낸다.
* stdout: 자식 프로세스 데이터를 출력한다.
* stderr: 명령에서 발생한 에러를 출력한다.

### 이용 예시
```javascript
import { spawn } from 'child_process';
let process = spawn('bash');
process.stdin.write(command);
process.stdin.end(); 
process.on('close', function (code) {
        console.log('end')
});
```
위와 같은 방법으로 자식 프로세스에서 터미널 커맨드를 작동시킨다.  
stdin을 이용할 경우 end()로 끝내주어야 하고, spawn()은 stream을 이용하기 때문에 이벤트가 끝났을 경우 close 이벤트로 감지 할 수 있다.

### spawn vs exec
* spawn()
  * 쉘을 생성하지 않는다.
  * 하위 프로세스에서 반환된 데이터 스트리밍으로 인해 데이터 흐름이 일정하다.
  * 데이터 전송 크기 제한이 없다.


* exec()
  * 전달된 명령이 실행되는 쉘을 생성한다.
  * 데이터를 버퍼링 한다(프로세스가 닫힐 때까지 기다렸다가 데이터를 덩어리로 전송)
  * Node.js v.12.x 이전 최대 데이터 전송량은 200kb(기본값), 이후 1MB(기본값)

프로세스 완료에만 관심이 있다면 'exec'가 적합하다. Spawn은 ondata 이벤트와 함께 stdout 및 stderr에 대한 스트림을 열고 exec는 stdout 및 stderr이 있는 버퍼를 문자열로 반환한다.

