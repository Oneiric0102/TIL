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
}