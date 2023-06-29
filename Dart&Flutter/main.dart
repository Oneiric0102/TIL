mixin Strong{
  final double strenghtLevel = 1500.99;
}

mixin QuickRunner {
  void runQuick(){
    print("ruuuuuuuuun!");
  }
}

class Human {
  final String name;
  Human({required this.name});
  void sayHello(){
    print("Hi my name is $name");
  }
}
abstract class Gamer {
  void typing();
}

enum Team {red, blue}

class Player extends Human with Strong, QuickRunner{
  int xp;
  final Team team;
  int age;

  Player({
    required String name,
    required this.xp, 
    required this.team, 
    required this.age
  }) : super(name : name);

  Player.createBluePlayer({
    required String name, 
    required int age
  })  : this.age = age,
        this.team = Team.blue,
        this.xp = 0,
        super(name : name);

  Player.createRedPlayer(String name, int age)  : 
        this.age = age,
        this.team = Team.red,
        this.xp = 0,
        super(name : name);

  @override
  void sayHello(){
    super.sayHello();
    print('and I play fir ${team}');
  }

  void typing(){
    print("I'm typing");
  }
}

class Coach extends Gamer{
  void typing(){
    print("The Coach is typing");
  }
}

typedef ListOfInts = List<int>;

String sayHello({
    required String name,
    required int age,
    String country = 'korea'}) {
  return "Hello $name, you are $age, and you come from $country";
}

String capitalizeName(String? name) => name?.toUpperCase()??'UNKNOWN';

ListOfInts reverseListOfNumbers(ListOfInts list){
  var reversed = list.reversed;
  return reversed.toList();
}
void main(){
  print(sayHello(
    name:'Oneiric',
    age: 26,
    ));
  
  capitalizeName('oneiric');
  capitalizeName(null);

  reverseListOfNumbers([1,2,3]);

  var player = new Player(
    name: "nico",
    xp: 1500,
    team: Team.blue,
    age: 21,
  );
  player.sayHello();
  var redPlayer = Player.createRedPlayer("lynn", 12);
  redPlayer.sayHello();
  redPlayer
  ..xp = 1200
  ..age = 26;
}