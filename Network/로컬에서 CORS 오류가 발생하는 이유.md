로컬의 리소스를 요청할 때의 origin은 null이기 때문이다. 
즉, A경로/index.html에서 ajax를 통해 A경로/js/module.js에 리소스를 요청한다면 동일 경로의 리소스를 요청한 것이 아니고   
 A경로/index.html에서 null/js/module.js로 리소스를 요청한 것이 되어 CORS에러가 발생한다.
