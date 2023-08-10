typedef Word = Map<String, String>;

class Dictionary{
  List<Word> words = [];

  void add({
    required String term,
    required String definition
  }){
    words.add({"term" : term, "definition" : definition});
  }

  String get(String term){
    String definition = "단어가 존재하지 않습니다.";
    words.forEach((word) {
      if(word["term"] == term){
        definition = word["definition"]!;
      }
    });
    return definition;
  }

  void delete(String term){
    for(var i = 0; i<words.length;i++){
      if(words[i]["term"]==term){
        words.remove(words[i]);
        return;
      }
    }
  }

  void update({
    required String term,
    required String definition
  }){
      for(var i = 0; i<words.length;i++){
      if(words[i]["term"]==term){
        words[i]["definition"] = definition;
        return;
      }
    }
  }

  void showAll(){
    words.forEach((word) {
      print("term : ${word["term"]}, definition : ${word["definition"]}");
    });
    print("\n");
  }

  int count(){
    return words.length;
  }

void upsert({
    required String term,
    required String definition
  }){
      for(var i = 0; i<words.length;i++){
        if(words[i]["term"]==term){
          words[i]["definition"] = definition;
          return;
        }
      }
      words.add({"term" : term, "definition" : definition});
  }

  bool exists(String term){
    bool definition = false;
    words.forEach((word) {
      if(word["term"] == term){
        definition = true;
      }
    });
    return definition;
  }

  void bulkAdd(List<Word> add_words){
    add_words.forEach((word) {
      add(term: word["term"]!, definition: word["definition"]!);
    });
  }

  void bulkDelete(List<String> del_words){
    del_words.forEach((word) {
      delete(word);
    });
  }
}


void main(){
  var dict = Dictionary();
  dict.add(term: "김치", definition: "대박이네~");
  dict.add(term: "아파트", definition: "비싸네~");
  dict.bulkAdd([{"term" : "게임", "definition" : "재밌네~"}, {"term" : "치킨", "definition" : "맛있네~"}]);
  print(dict.count());
  print(dict.exists("김치"));
  print(dict.exists("컴퓨터"));
  dict.showAll();

  print(dict.get("김치"));
  print(dict.get("게임"));

  dict.delete("김치");
  dict.showAll();

  dict.update(term: "게임", definition: "하고싶네~");
  dict.showAll();

  dict.upsert(term: "게임", definition: "재밌네~");
  dict.upsert(term: "허브", definition: "향기롭네~");
  dict.showAll();
  
  dict.bulkDelete(["게임", "치킨"]);
  dict.showAll();
}