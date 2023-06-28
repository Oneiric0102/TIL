# Dart
## Dart Native
    Dart는 개발중일때는 JIT 컴파일러를, 배포할때는 AOT 컴파일러를 사용한다.
- AOT(Ahead-Of-Time) : C, C++ 등으로 코딩할 때 처럼 컴파일 후 그 결과인 바이너리를 배포하는 것
- JIT(Just-In-Time) : dart VM을 사용해 코드의 결과를 바로 보여주는 것

## 변수
- var : Dart에서는 var를 사용해서 변수를 초기화 하면 컴파일러가 초기화된 값을 바탕으로 해당 변수의 타입을 알아낸다. 변수는 업데이트 될 수 있으며 초기화값과 같은 타입이어야 한다. 혹은 String과 같이 타입을 명시할 수도 있다.
- Dynamic type : var 변수를 초기화하지 않거나 dynamic 으로 명시하면 해당 변수는 Dynamic Type이 된다. Dynamic Type은 어떤 타입의 값이든 업데이트가 가능하다.
- Nullable variables : Null Safety를 보장하기 위해 해당 변수가 Null일수도 있음을 명시하는것이다. String? 처럼 타입명 옆에 ?를 붙여서 사용한다. '변수명?.method' 를 하면 변수가 null이 아닐경우 method를 호출할 수 있다.
- Final variables : C의 const처럼 수정이 불가능한 변수이다. var 대신 final 키워드를 써서 사용할 수 있다.
- late variables : 변수를 먼저 선언하고 초기화는 나중에 할 수 있는 변수이다. 보통 api 작업할 때 많이 사용되며 변수에 값이 할당되기 전에는 호출이 되지 않으므로 Null Safety가 보장된다.
- Constant variables : 컴파일 타임에 값을 알고있는 상수이다.

## 자료형
    Dart에서 대부분의 타입은 객체로 이루어져 있다.

### 기본 자료형
- int : 정수형
- double : 실수형
- String : 문자열
- bool : True, False
- num : int와 double의 부모 클래스로, num으로 타입을 정의하면 정수와 실수를 모두 할당할 수 있다.
- Map : Map<Stirng, object> = {'name' : 'Oneiric', 'xp' : 19.99,};
- Set : 리스트와는 달리 속한 아이템들이 모두 유니크한 집합, Set<int> numbers = {1, 2, 3, 4};

### 리스트
    변수들의 집합으로 아래와 같은 문법을 사용한다.
        var oldFriends = ['nico', 'lynn'];
        var newFriends = [
            'lewis',
            'ralph',
            if(condition) 'darren'
            for(var friend in oldFriends) "Best Friend $friend",
        ]
- collection if : 리스트를 생성할 때 if(condition) value 와 같이 작성하면 condition이 true일 때 value가 리스트에 추가된다.
- collection for : 리스트를 생성할 때 for(item in list) "~~~ $item"와 같이 작성하면 list의 값이 변형되어 추가된다.

## 함수
    Dart의 함수는 객체이며, 아래와 같은 기능들이 제공된다.
- Named Parameters : 함수 호출 시 매개변수명을 사용해서 매개변수를 넘겨줄 수 있다.
- Optional Positional Parameters : 함수 호출 시 매개변수명을 사용해서 매개변수를 넘겨주지 않더라도 특정 매개변수가 필수 요소가 아님을 명시할 수 있다.
- QQ Operator : 좌항이 null이면 우항을, null이 아니면 좌항을 반환한다.
- QQ Equals : 좌항이 null이라면 우항을 좌항에 할당한다.
- Typedef : 자료형이 헷갈리지 않도록 도움이 될 alias를 만드는 것이다.