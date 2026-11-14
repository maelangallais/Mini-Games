# 🎮 Mini-Games

A compact collection of standalone **NumWorks MicroPython** games that are complete and fun to play without needing their own dedicated repository.

---

## 📂 Scripts Included

### Connect 4
[`connect4.py`](connect4.py) · *Created May 15, 2023*

Classic two-player **Connect 4** (`7 × 6` grid) rendered with `kandinsky`:
- Tracks games played, red wins, yellow wins, and draws on a live side scoreboard.
- Includes a pixel-art Toad sprite in the bottom-right corner to fill the empty sidebar space.
- **Controls**: `Left` / `Right` to select a column, `OK` to drop a disc, and restart prompts between rounds.

### World Flags Quiz
[`flags_quiz.py`](flags_quiz.py) · *Created March 08, 2023*

Interactive geography quiz rendering **12 world flags** directly on screen with `kandinsky` (including custom rotated ellipse rendering for angled emblems):
- Displays each flag graphically and prompts you to identify the country.
- Tracks your score across the quiz.

---

## 🖥️ Requirements & Platform

- MicroPython for **NumWorks** calculators (`kandinsky`, `ion`, `math`, `random`, `time`).
