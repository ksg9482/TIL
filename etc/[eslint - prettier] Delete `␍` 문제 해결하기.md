# [eslint - prettier] Delete `␍` 문제 해결하기

### 빠른 결론
결론부터 말하면 줄바꿈 옵션 때문에 발생한 문제다. 거기에 더해 prettier 버전 문제도 있다.

.eslintrc.js 파일 rules에 {endOfLine: 'auto'} 를 설정하면 된다.

### 원인
LF, CR은 줄을 바꾸는 방식에 대한 설정값이다.
* LF: Line Feed(\n) - 현재 커서의 위치에서 커서의 위치변화 없이 한 줄 아래로 내리는 방식
* CR: Carriage Return(\r) - 현재 줄에서 커서의 위치를 맨 앞으로 옮기는 방식

윈도우에서 엔터를 눌러 줄바꿈을 시도하면 CRLF(\r\n) 방식으로 적용되기 때문에 커서가 가장 앞으로 옮겨지고 아래로 한 칸 내려가게 된다.

하지만 prettier 2.0에서 endOfLine 기본 값이 LF로 지정되었기 때문에 그 이하버전을 사용하다가 git pull 등으로 2.0이상 버전을 만나게 되면 에러가 발생한다.

### endOfLine
auto는 각 os에 설정된 값을 이용하라는 구문이다.

prettier 2.0 이전 기본값은 기존 파일들의 호환성을 위해 'auto'였으나,  2.0에서 기본 값이 LF로 지정되었다.

prettier 측이 밝히는 이유는 개행 문자로 인해 git diff과 git blame의 어려움을 제거하고자 LF를 사용하기로 했다고 한다.

#### 참조
[https://prettier.io/blog/2020/03/21/2.0.0#breaking-changes](https://prettier.io/blog/2020/03/21/2.0.0#breaking-changes)
