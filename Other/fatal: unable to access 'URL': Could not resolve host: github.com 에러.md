# fatal: unable to access 'https://github.com/ksg9482/TagMark_Backend/': Could not resolve host: github.com

### 원인
깃허브 저장소에 접근하지 못해 발생하는 에러이며 보통 proxy가 원인이 된다.

### 해결
git config --global --unset http.proxy   
git config --global --unset https.proxy

또는 공유기 등 네트워크 쪽 문제이다.
