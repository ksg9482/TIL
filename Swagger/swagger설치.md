npm install swagger-cli swagger-ui-express
npm install -D @types/swagger-ui-express

swagger 폴더 생성, swagger.js 생성 -> json export 

swagger 홈페이지 참조
https://editor.swagger.io/


"servers": [
    {
      "url": "백엔드 주소"
    }
  ]
부분이 접속할 백엔드 주소

익스프레스에 적용
app.use('/api-json', swaggerUi.serve, swaggerUi.setup(swaggerJson))

'/api-json'는 백엔드 주소 뒤에 붙히면 swagger에 접속할 수 있다.
