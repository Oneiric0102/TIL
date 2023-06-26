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