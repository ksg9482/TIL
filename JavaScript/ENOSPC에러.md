### 에러: Internal watch failed: ENOSPC: System limit for number of file watchers reached, watch <주소>
### 원인:
Nodemon에서 발생하는 에러이다.   
시스템이 허용하는 것 보다 더 많이 접근했을 때 발생하는 오류인데 ENOSPC는 nodejs에서 드라이브에 공간이 없다는 의미로 사용되는 에러 코드라고 한다. 이 경우 드라이브에 공간이 없는 상황은 아니니 어떤 의미로든 공간이 없으면 해당 에러 코드를 사용하는 것 같다.   
### 해결: max watches를 높게 설정한다.
* echo fs.inotify.max_user_watches=582222 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
* 어떤 프로세스가 파일 감시자를 사용하고 있는지 확인하려면 아래 명령을 사용한다. root 사용자로 들어가서 실행해야 한다.
```javascript
find /proc/*/fd -lname anon_inode:inotify |
cut -d/ -f3 |
xargs -I '{}' -- ps --no-headers -o '%p %U %c' -p '{}' |
uniq -c |
sort -nr
```
### 의문:
* 분명 어제까지만 해도 멀쩡히 돌아갔고, 그 사이 바뀐것도 없다. 도대체 왜 이 에러가 발생했을까?
* max watches를 이용해 해결한다고 하지만 이게 최선일까? 부작용은 없는 건가?

### 레퍼런스
[https://mytory.net/archives/13120](https://mytory.net/archives/13120)   
[https://stackoverflow.com/questions/34662574/node-js-getting-error-nodemon-internal-watch-failed-watch-enospc](https://stackoverflow.com/questions/34662574/node-js-getting-error-nodemon-internal-watch-failed-watch-enospc)
