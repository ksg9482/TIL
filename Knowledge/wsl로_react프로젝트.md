# wsl로 react프로젝트를 실행할 때

wsl로 react프로젝트를 실행할 때 주의점이 있다. 바로 wsl 폴더에 프로젝트를 생성해야 한다는 것이다. wsl에서 바로 접근가능한 폴더가 아니라 다른 저장소에 프로젝트를 생성하면 npm start를 실행했을때 반응이 굉장히 느려지고, 프로젝트 용량이 크면 클수록 이 시간차이는 극단적이다.