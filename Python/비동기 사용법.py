```python
import asyncio

import requests

# A few handy JSON types
JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]
JSONList = list[JSON]


def http_get_sync(url: str) -> JSONObject:
    response = requests.get(url)
    return response.json()

async def http_get(url: str) -> JSONObject:
    return await asyncio.to_thread(http_get_sync, url)

"""
http 요청을 보내는 http_get_sync 함수와, 이 함수를 비동기로 바꾸는 http_get 함수.
동기적으로 http 요청을 기다리는 경우도 비동기와 함께 사용하기 쉽다.
여러 api 요청을 수행하는 것을 효율적으로 만들수 있다.
"""
```

```python
"""

동시 컴퓨팅과 병렬 컴퓨칭
병렬 컴퓨팅은 응용프로그램이 여러 작업을 동시에 수행. 각 작업이 별도의 처리장치에서 수행됨을 의미.
두 명의 종업원이 두 줄의 고객의 요청을 처리한다.

동시 컴퓨팅은 애플리케이션이 작업 a, 작업 b를 수행할 때 실제 병렬로 실행하는 대신 작업을 전환하며 수행함을 의미. 이 두 작업은 a를 먼저 끝낼 필요가 없다. 단, 동시 컴퓨팅은 작업간 전환이라는 비용이 필요하다.
한 명의 종업원이 두 줄의 고객을 번갈아가며 처리한다.

파이썬은 GIL(Global Interpreter Lock)이 있다. 코드는 인터프리터에서 lock을 획득해야 한다. 이는 파이썬 코드에서 여러 스레드를 사용 하더라도 파이썬은 단일 스레드로 처리함을 의미한다.
그래서 파이썬 동시 프로그래밍은 여러 프로세스를 사용하거나 lock을 할 필요가 없는 인터프리터로 전환해야 한다. 반면 동시성은 파이썬 3.10부터 잘 작동한다.

동시성이 컴퓨팅을 잘 수행하는 현명한 방법인 이유는 많은 작업이 대기를 포함하거나 애플리케이션이 파일을 읽고 쓸때까지 기다리거나, 인터넷 통신, 사용자 입력 대기가 발생하기 때문이다. 이 대기시간을 효율적으로 다룰 수 있는 중요한 메커니즘인 것이다.

파이썬은 asyncio를 통해 동시성을 지원하며, 이는 메서드나 함수 앞에 async 키워드를 사용하여 메서드나 함수가 동시 실행될 수 있음을 나타내는 것이다.
동시 메서드 앞에 await 키워드를 사용하면 작업이 실행되는 순서를 제어할 수 있다. await 키워드 이하의 코드는 해당 작업이 완료되어야 실행될 수 있음을 나타낸다.
이는 코드가 앞부분의 결과에 의존할 때 중요하다. 데이터 베이스에서 값을 가져오거나 로그인 확인 등이 대표적인 경우다.
"""

import asyncio
from random import randint
from time import perf_counter
from typing import AsyncIterable

from req_http import http_get, http_get_sync

MAX_POKEMON = 898


def get_random_pokemon_name_sync() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = http_get_sync(pokemon_url)
    return str(response["name"])

async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = await http_get(pokemon_url)
    return str(response["name"])

"""
파이썬 3.10부터 async/await가 잘 통합되어 있다. 몇가지 다루는 방법이 있고, 그 중 한가지가 async/await 구문을 generator와 결합하는 것이다.
"""

# AsyncIterable: 비동기 반복가능 객체
async def next_pokemon(total:int) -> AsyncIterable[str]:
    """
    total만큼의 랜덤 포켓몬 이름을 반환
    """
    for _ in range(total):
        # name = await get_random_pokemon_name()
        result = await asyncio.gather(*[get_random_pokemon_name() for _ in range(20)])
        # generator
        yield result

async def main() -> None:
    # 비동기와 생성기를 결합해서 사용할 수 있다. -> 비동기 함수이므로 생성기 내부에서 비동기를 활용 할 수 있다.
    time_before = perf_counter()
    names = [name async for name in next_pokemon(2)]
    print(names)
    # async for name in next_pokemon(20):
    #     print(name)
    print(f"Total time (asynchronous): {perf_counter() - time_before}.")


    # # 비동기지만 동기적으로 실행
    # time_before = perf_counter()
    # for _ in range(20):
    #     # 단일 http 요청이면 비동기의 효과를 느끼기 어려움.
    #     # 이전 요청이 완료되기 전에 다음 요청을 보낼 수 없어서 만족할 성능을 얻지 못한다. 
    #     pokemon_name = await get_random_pokemon_name()
    #     print(pokemon_name)
    # print(f"Total time (synchronous): {perf_counter() - time_before}.")
    
    # # 비동기 asyncio.gather
    # time_before = perf_counter()
    # # asyncio.getter를 사용하여 for루프에 대한 대안을 작성할 수 있다.
    # # 여러 비동기 함수를 동시에 실행하고, list comprehension을 사용하여 문자열 tuple을 얻는다.
    # result = await asyncio.gather(*[get_random_pokemon_name() for _ in range(20)])
    # print(result)
    # print(f"Total time (asynchronous): {perf_counter() - time_before}.")


if __name__ == "__main__":
    # 비동기로 main()을 실행
    asyncio.run(main())
```

```python
import asyncio
import time
import requests

# 카운터를 시작한 다음 범위로 이동하는 비동기 카운터 함수
async def counter(until: int = 10) -> None:
    now = time.perf_counter()
    print("Started counter")
    for i in range(1, until):
        last = now
        await asyncio.sleep(0.01)
        now = time.perf_counter()
        # 몇 밀리초 동안 잠자기 상태인 내용을 출력
        print(f"{i}: Was asleep for {now - last}s")

# http 요청을 보내는 동기 함수
def send_request(url: str) -> int:
    print("Sending HTTP request")
    response = requests.get(url)
    return response.status_code

# 이 함수는 asyncio.to_thread를 반환한다. 
# 전송 요청을 비동기 전송 요청으로 전환하는 데 사용할 함수.
async def send_async_request(url: str) -> int:
    # send_request를 asyncio.to_thread로 래핑하여 비동기 함수로 동작하게 한다.
    # 비동기로 요청을 보내고 값을 기다려야 하기 때문에 await를 사용한다.
    return await asyncio.to_thread(send_request, url)

async def main() -> None:
    # # 동기 함수가 처리되기 전까지는 비동기 함수가 실행되지 않는다.
    # # http 요청을 보내는 순간 lock이 걸리기 때문에 동시 코드가 아니게 된다.
    # status_code = send_request("https://www.arjancodes.com")
    # print(f"Got HTTP response with status {status_code}")
    # await counter()

    # # 해결법 시도 1. 비동기 task 생성
    # # 태스크를 만들고 카운터 함수에 대한 호출을 제공
    # # 작업을 동시에 수행한다. 하지만 변한점은 없다.
    # task = asyncio.create_task(counter())
    # status_code = send_request("https://www.arjancodes.com")
    # print(f"Got HTTP response with status {status_code}")
    # await task

    # 해결법 시도 2. asyncio.gather 사용
    # 하지만 전송 요청이 동시적이기 때문에 작동하지 않는다.
    # 따라서 정말 해야하는 일은 request요청을 비동기 함수로 바꾸는 것이다.

    # # 해결법 1. 동기함수를 비동기 함수로 전환
    # # 카운터 태스크와 http 요청이 동시에 실행된다.
    # task = asyncio.create_task(counter())
    # status_code = await send_async_request("https://www.arjancodes.com")
    # print(f"Got HTTP response with status {status_code}")
    # await task

    # 해결법 2. 비동기 함수가 되었으므로 asyncio.gather를 사용할 수 있다.
    status_code, _ = await asyncio.gather(
        send_async_request("https://www.arjancodes.com"),
        counter()
    )

asyncio.run(main())
```
