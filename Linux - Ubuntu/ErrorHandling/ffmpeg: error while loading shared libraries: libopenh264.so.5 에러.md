### ffmpeg: error while loading shared libraries: libopenh264.so.5 에러 발생시 해결법

```
ffmpeg: error while loading shared libraries: libopenh264.so.5:
cannot open shared object file: No such file or directory
```
해결법에서 가장 많이 보이는 방식은 conda update ffmpeg 명령어로 ffmpeg를 업데이트 하는 것이었다.    
하지만 해결되지 않아서 재설치까지 했으나 마찬가지 였다. 원인을 찾다보니 python 3.8이 너무 새롭기 때문이라는 글을 보았다. 

마침 이용해야 하는 것도 python 3.8에  ffmpeg 4.3.2 버전이니 상황이 굉장히 유사했다. 
제시된 해결법은 libopenh264.so 파일을 복사해서 libopenh264.so.5을 대체하는 것이다.
```
ln -s ~/anaconda3/lib/libopenh264.so ~/anaconda3/envs/py38/lib/libopenh264.so.5

cp libopenh264-2.1.0-linux64.5.so ~/anaconda3/envs/my_env/lib/libopenh264.so.5

~/anaconda3/lib/libopenh264.so 복사해서 이름 변경
```
혹시나 해서 파일명을 검색해보니 libopenh264.so랑  libopenh264.so.6은 있는데 libopenh264.so.5는 없었다.
libopenh264.so 파일을 복사해서 libopenh264.so.5로 이름을 바꿔 해결했다.

##### 출처
[https://stackoverflow.com/questions/62213783/ffmpeg-error-while-loading-shared-libraries-libopenh264-so-5](https://stackoverflow.com/questions/62213783/ffmpeg-error-while-loading-shared-libraries-libopenh264-so-5)
