Langchain + Ollama + Local LLM을 이용하여 프로젝트를 진행하고 있다.

최근 가장 헤맸던 일은 OllamaFunctions를 사용하는 일이었다. OllamaFunctions은 Ollama를 통해 LLM을 이용할 때 function calling을 이용할 수 있게 해주는 래퍼 클래스이다. langchain_experimenal에 속한 실험적인 기능이라 더 불안정하다.

일단 다른 사람들은 어떻게 사용하나 레퍼런스를 찾으면 다른 사람의 프로젝트는 문제없이 동작하고, 공식 가이드북도 별다른 문제가 보이지 않는다.

하지만 내 코드는 동작하지 않는다...... 나 뿐만 아니라 동작하지 않는다는 문의는 많고, 실제로 깃허브 이슈를 보면 유사한 이슈가 많이 보인다.

결론부터 말하면 현재(langchain-experimental 0.0.59)기준 pip 패키지와 github 내용이 안맞는다. github에 있는 소스코드에는 구현이 되어있었다. 그저 pip에 내용이 없었기에 내 컴퓨터에 있는 langchain 패키지에도 내용이 없을 뿐이었다.

langchain 자체가 급속도로 성장하고 있는 프레임워크이고, 기능도 추가, 수정이 빈번하여 발생한 일로 파악하고 있다. github 이슈를 살펴보면 이에 대해 인지하고 있는 것 같다. 아직 불안정하고 실험적인 시도라 조심스러운 것일까?

https://stackoverflow.com/questions/78404535/langchain-python-with-structured-output-ollama-functions

위 링크에서 완전히 같은 내용은 아니지만 문제의 원인을 찾을 수 있었다.

OllamaFunctions는 BaseChatModel을 상속 받았지만 bind_tools 함수는 따로 구현되어 있지 않다. BaseChatModel에 있는 bind_tools은 NotImplementedError예외를 일으킨다.

```python
def bind_tools(
	self,
	tools: Sequence[Union[Dict[str, Any], Type[BaseModel], Callable, BaseTool]],
	**kwargs: Any,
) -> Runnable[LanguageModelInput, BaseMessage]:
	raise NotImplementedError()
```

임시로 조치할 수 있는 솔루션은 github에 있는 내용을 로컬 모듈로 만들어 사용하는 것이다. 최신? OllamaFunctions에는 bind_tools이 구현되어 있다.

```python
def bind_tools(
	self,
	tools: Sequence[Union[Dict[str, Any], Type[BaseModel], Callable, BaseTool]],
	**kwargs: Any,
) -> Runnable[LanguageModelInput, BaseMessage]:
	return self.bind(functions=tools, **kwargs)
``` 

나도 bind_tools이 구현되었다는 깃허브 이슈를 보고 처리된 줄 알았는데 설마 상황이 이럴줄은... 금방 필요하지 않게 될 팁이지만 뭔가 이상하면 어딜 살펴보면 되겠다 하는 경험을 쌓았다는 일에 의미를 두자.

유기적으로 맞물려있는 소스코드를 고려하면 정말 임시변통이지만 아예 안되던 코드를 동작할 준비가 된 코드로 만드는데 조금이라도 도움이 될 것이라 본다.

참고로 function calling에 사용하는 additional_kwargs에 사용되는 키가 function_call, tool_calls이 있는데(둘 역할이 조금 다르다.) 키가 혼동된다는 이슈도 보인다. 이 키에 관해서 수정할 것이라는 코멘트가 있었기에 업데이트 될 때 유심히 살펴야 할 것 같다.
