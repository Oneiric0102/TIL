# Flutter
## Flutter란?
    구글에서 개발 및 지원하는 오픈 소스 프레임워크로, 크로스플랫폼 개발에 적합하다. Flutter가 출시되었을 때에는 모바일 앱 개발이 주를 이루었으나, 현재는 iOS, Android, 웹, Windows, MacOS, Linux의 여섯 가지 플랫폼에 대한 애플리케이션 개발을 지원한다.
### Flutter의 작동방법
    Flutter는 Dart로 작성된 코드를 Flutter Framework가 이용하면, 엔진이 해당하는 UI를 그려주는 방식으로 작동한다. 따라서 Flutter는 운영체제와 직접 소통하지 않으며 따라서 내장된 플랫폼 widget을 사용할 수 없다. 대신에 Flutter는 크로스플랫폼 언어임에도 불구하고 네이티브에 가까운 성능을 보여주며, 커스터마이징 된 UI를 구성하는것이 비교적 간단하다.

## 위젯
    플러터의 화면에 그려지는 모든 요소는 위젯으로 구성되어 있다. 플러터는 기본 위젯을 제공함과 동시에 앱 개발자가 위젯을 직접 만들수도 있다.
- Stateless Widget : build 메서드를 통해서 단순히 UI를 출력하는 위젯
- Stateful Widget : 데이터가 변경될 때 변화가 UI에 반영되어 실시간으로 볼 수 있는 위젯, setState 함수를 사용해서 리랜더링 할 수 있다.
- BuildContext : 위젯 트리 안에서 위젯의 위치를 다룰 수 있게 해주는 요소

### 위젯의 종류
- MaterialApp : 페이지의 구성요소를 최상단에서 담는 위젯
- Scaffold : 기본적인 앱에서 디자인의 뼈대를 구성하는 위젯
- Column : 매개변수로 입력받은 위젯들을 세로로 배치
- Row : 매개변수로 입력받은 위젯들을 가로로 배치
- SizeBox : 높이와 너비를 지정해서 해당하는 크기의 Box를 만들어주는 위젯
- Text : 화면에 문자열을 표시하는 위젯
- TextStyle : Text 위젯의 스타일을 조정하는 위젯
- Padding : Padding을 설정하는 위젯
- Container : child를 가지고 있는 단순한 box, html과 div와 같은 역할
- Flexable : Flex 레이아웃을 사용할 수 있는 위젯
- FutureBuilder : 비동기 처리를 위해 사용하는 위젯, Future값을 기다리고 데이터가 존재하는지를 알려줌
- ListView : 목록을 보여주는것에 최적화된 위젯, .builder를 사용하면 화면에 보이는 데이터만 로딩 할 수 있음