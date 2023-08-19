import 'package:flutter/material.dart';
import 'package:flutter_practice/screens/home_screen.dart';

void main() {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        colorScheme: ColorScheme.fromSwatch(
          backgroundColor: const Color(0xFFE24C3C),
        ),
        textTheme: const TextTheme(
          displayLarge: TextStyle(
            color: Color(0xFFE24C3C),
          ),
          displaySmall: TextStyle(
            color: Color(0xFFF6A79C),
          ),
        ),
        cardColor: const Color(0xFFFBF6F4),
      ),
      home: HomeScreen(),
    );
  }
}
