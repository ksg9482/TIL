# static factory method에 대해
## 개요
private를 통해 클래스 외부의 접근을 차단하는 것과 이를 보다 유연하게 이용하기 위해 static method를 이용하는 것에 대해 고민이 있다.
일단 스태틱 메서드로 생성하는 방법은 크게 두종류 있는 것 같다. 하나는 생성자를 이용하는 것이고 다른 하나는 생성자를 이용하지 않는 것이다.

### 생성자를 이용하는 방법
생성자를 private로 설정하고 static 메서드로 클래스 내부에서 생성자에 입력한다. 간단하게 표현하자면 다음과 같을 것이다.
```typescript
class Post {
    private _id: number;

    private constructor(
      id: number
    ) {
      this._id = id;
    }

    get id(): number {
      return this._id;
    }

    static from(id: number) {
      const post = new Post(id);
      return post;
    }
}
```

### 생성자를 이용하지 않는 방법
아예 생성자를 비워두고, static 메서드를 클래스 내부에서 생성하는 것은 같지만 생성한 인스턴스에 필드에서 값을 할당한다. 간단하게 표현하자면 다음과 같을 것이다.
```typescript
class Post {
    private _id: number;

    get id(): number {
      return this._id;
    }

    static from(id: number) {
      const post = new Post();
      post._id = id;
      return post;
    }
}
```

### 고민
둘 다 충분히 사용할 수 있는 방법이지만 뭐가 더 일반적으로 사용할 범위가 넓은 방법일까? 

그리고 인자를 받는 방식도 고민이다. 규격화된 객체를 전해줘도 되고, 필요한 요소를 담은 객체를 받도록 타입을 구성해도 되고, 그냥 여러개 인자를 받도록 해도 된다.
```typescript
{
  class Post {
    private _id: number;
    private _title: string;
    private _content: string;
    private _createdAt: Date;

    // constructor() {}

    get id(): number {
      return this._id;
    }

    get title(): string {
      return this._title;
    }

    get content(): string {
      return this._content;
    }

    get createdAt(): Date {
      return this._createdAt;
    }
  }
  class PostDto {
    private _id: number;
    private _title: string;
    private _content: string;
    private _createdAt: string;

    // constructor() {} //생성자가 들어가있어야 클래스로서 동작한다. 없으면 그냥 데이터구조와 다를바 없다.

    get id(): number {
      return this._id;
    }

    get title(): string {
      return this._title;
    }

    get content(): string {
      return this._content;
    }

    get createdAt(): string {
      return this._createdAt;
    }

    //최선의 방법은?
    static from(post: Post) {
      const postDto = new PostDto();
      postDto._id = post.id;
      postDto._title = post.title;
      postDto._content = post.content;
      postDto._createdAt = post.createdAt.toISOString();
      return postDto;
    }

    static from2(post: {
      id: number;
      title: string;
      content: string;
      createdAt: Date;
    }) {
      const postDto = new PostDto();
      postDto._id = post.id;
      postDto._title = post.title;
      postDto._content = post.content;
      postDto._createdAt = post.createdAt.toISOString();
      return postDto;
    }

    static from3(id: number, title: string, content: string, createdAt: Date) {
      const postDto = new PostDto();
      postDto._id = id;
      postDto._title = title;
      postDto._content = content;
      postDto._createdAt = createdAt.toISOString();
      return postDto;
    }
  }
}

```
