import 'dart:async';

import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  static const timeButtonWidth = 82;
  static const halfScreen = 205;
  static const maxRounds = 4;
  static const maxGoals = 12;
  int totalSeconds = 1500;
  late Timer timer;
  bool isRunning = false;
  bool isBreakTime = false;
  int rounds = 0;
  int goals = 0;
  int breakTime = 600;
  int selectedTime = 25;
  final ScrollController _scrollController = ScrollController(
    initialScrollOffset: 4.5 * timeButtonWidth - halfScreen,
    keepScrollOffset: true,
  );

  void onTick(Timer timer) {
    if (totalSeconds == 0) {
      if (isBreakTime) {
        setState(() {
          isRunning = false;
          isBreakTime = false;
          totalSeconds = selectedTime * 60;
        });
        timer.cancel();
      } else {
        rounds++;
        if (rounds == maxRounds) {
          if (goals < maxGoals) {
            rounds = 0;
            goals++;
          }
        }
        setState(() {
          isBreakTime = true;
          totalSeconds = breakTime;
        });
      }
    } else {
      setState(() {
        totalSeconds = totalSeconds - 1;
      });
    }
  }

  void onStartPressed() {
    timer = Timer.periodic(
      const Duration(seconds: 1),
      onTick,
    );
    setState(() {
      isRunning = true;
    });
  }

  void onPausePressed() {
    timer.cancel();
    setState(() {
      isRunning = false;
    });
  }

  String format(int seconds, bool isHour) {
    var duration = Duration(seconds: seconds);
    if (isHour) {
      return duration.toString().split('.').first.substring(2, 4);
    } else {
      return duration.toString().split('.').first.substring(5, 7);
    }
  }

  void reset() {
    if (isRunning) {
      timer.cancel();
      isRunning = false;
    }
    setState(() {
      isBreakTime = false;
      totalSeconds = selectedTime * 60;
    });
  }

  void timeSet(int time) {
    if (isRunning) {
      timer.cancel();
      isRunning = false;
    }
    setState(() {
      totalSeconds = time * 60;
      selectedTime = time;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Theme.of(context).colorScheme.background,
      body: Column(
        children: [
          //Status Bar margin
          const SizedBox(
            height: 20,
          ),
          //Header
          Flexible(
            fit: FlexFit.loose,
            flex: 1,
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 35.0),
              child: Container(
                alignment: Alignment.centerLeft,
                child: Text(
                  "POMOTIMER",
                  style: TextStyle(
                    color: Theme.of(context).cardColor,
                    fontSize: 22,
                    fontWeight: FontWeight.w600,
                  ),
                ),
              ),
            ),
          ),
          //Timer display
          Flexible(
            fit: FlexFit.tight,
            flex: 3,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Stack(
                  alignment: Alignment.bottomCenter,
                  children: [
                    Container(
                      width: 123,
                      height: 182,
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: Theme.of(context).cardColor.withOpacity(0.7),
                        borderRadius: const BorderRadius.all(
                          Radius.circular(5),
                        ),
                      ),
                    ),
                    Container(
                      width: 135,
                      height: 177,
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: Theme.of(context).cardColor.withOpacity(0.7),
                        borderRadius: const BorderRadius.all(
                          Radius.circular(5),
                        ),
                      ),
                    ),
                    Container(
                      width: 150,
                      height: 170,
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: Theme.of(context).cardColor,
                        borderRadius: const BorderRadius.all(
                          Radius.circular(5),
                        ),
                      ),
                      child: Text(
                        format(totalSeconds, true),
                        style: TextStyle(
                          color:
                              Theme.of(context).textTheme.displayLarge!.color,
                          fontSize: 80,
                          fontWeight: FontWeight.w800,
                        ),
                      ),
                    ),
                  ],
                ),
                Padding(
                  padding: const EdgeInsets.all(10.0),
                  child: Text(
                    ':',
                    style: TextStyle(
                      color: Theme.of(context).textTheme.displaySmall!.color,
                      fontSize: 60,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ),
                Stack(
                  alignment: Alignment.bottomCenter,
                  children: [
                    Container(
                      width: 123,
                      height: 182,
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: Theme.of(context).cardColor.withOpacity(0.7),
                        borderRadius: const BorderRadius.all(
                          Radius.circular(5),
                        ),
                      ),
                    ),
                    Container(
                      width: 135,
                      height: 177,
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: Theme.of(context).cardColor.withOpacity(0.7),
                        borderRadius: const BorderRadius.all(
                          Radius.circular(5),
                        ),
                      ),
                    ),
                    Container(
                      width: 150,
                      height: 170,
                      alignment: Alignment.center,
                      decoration: BoxDecoration(
                        color: Theme.of(context).cardColor,
                        borderRadius: const BorderRadius.all(
                          Radius.circular(5),
                        ),
                      ),
                      child: Text(
                        format(totalSeconds, false),
                        style: TextStyle(
                          color:
                              Theme.of(context).textTheme.displayLarge!.color,
                          fontSize: 80,
                          fontWeight: FontWeight.w800,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
          //Timer Set
          Flexible(
            fit: FlexFit.loose,
            flex: 1,
            child: ListView.builder(
              controller: _scrollController,
              scrollDirection: Axis.horizontal,
              itemBuilder: (ctx, index) {
                return UnconstrainedBox(
                  child: Container(
                    width: 66,
                    height: 50,
                    alignment: Alignment.center,
                    margin: const EdgeInsets.symmetric(
                      horizontal: 8,
                    ),
                    decoration: BoxDecoration(
                      color: ((index % 7 + 1) * 5 == selectedTime)
                          ? Theme.of(context).cardColor
                          : Colors.transparent,
                      border: Border.all(
                        color: Theme.of(context).cardColor,
                        width: 2,
                      ),
                      borderRadius: const BorderRadius.all(
                        Radius.circular(8),
                      ),
                    ),
                    child: TextButton(
                      onPressed: () {
                        timeSet((index % 7 + 1) * 5);
                      },
                      child: Text(
                        '${(index % 7 + 1) * 5}',
                        style: TextStyle(
                          fontSize: 26,
                          fontWeight: FontWeight.bold,
                          color: ((index % 7 + 1) * 5 == selectedTime)
                              ? Theme.of(context).textTheme.displayLarge!.color!
                              : Theme.of(context).cardColor,
                        ),
                      ),
                    ),
                  ),
                );
              },
            ),
          ),
          //Timer Start/Pause/Reset
          Flexible(
            fit: FlexFit.tight,
            flex: 3,
            child: Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  IconButton(
                    iconSize: 100,
                    color: Theme.of(context).cardColor,
                    onPressed: isRunning ? onPausePressed : onStartPressed,
                    icon: Icon(isRunning
                        ? Icons.pause_circle_filled
                        : Icons.play_circle_fill),
                  ),
                  TextButton(
                    onPressed: reset,
                    child: Text(
                      "Reset",
                      style: TextStyle(
                        color: Theme.of(context).textTheme.displaySmall!.color,
                        fontSize: 20,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
          //Rounds and Goals Display
          Flexible(
            fit: FlexFit.tight,
            flex: 2,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Text(
                        "$rounds/$maxRounds",
                        style: TextStyle(
                          color:
                              Theme.of(context).textTheme.displaySmall!.color,
                          fontSize: 28,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ),
                    Text(
                      "ROUND",
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.w600,
                        color: Theme.of(context).cardColor,
                      ),
                    ),
                  ],
                ),
                Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: Text(
                        "$goals/$maxGoals",
                        style: TextStyle(
                          color:
                              Theme.of(context).textTheme.displaySmall!.color,
                          fontSize: 28,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ),
                    Text(
                      "GOAL",
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.w600,
                        color: Theme.of(context).cardColor,
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
