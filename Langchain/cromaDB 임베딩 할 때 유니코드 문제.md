처음에는 임베딩 문제인줄 알았다. 
결론부터 말하면 vectorDB에 임베딩은 문제가 아니였다. 그 전 단계이다.

Langchain에서 JSON을 vectorDB에 임베딩 할 때 JSONLoader를 별도로 제공해준다. 
/uac00 형태로 유니코드 화 된 문자열은 유니코드를 인코딩해서 입력되는 것이 아니라 /uac00이 문자열로 임베딩되서 들어간다.

즉, 임베딩하기 위해 json을 읽을 때부터 처리를 해야 한다.
안타까운 점은 JSONLoader에 인코딩 설정하는 기능을 못찾겠다. 기본 UTF-8인데 한국어로 하면 읽을 때는 제대로 되지만 json.dumps로 저장할 때 ancii로 저장해서 정상작동을 안한다.
라이브러리에서 json.dumps(content, ensure_ascii=False)를 설정해 ancii로 바뀌지 않게 한다.
