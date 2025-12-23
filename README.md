# grim-reaper-academy


# Deadline Simulator (YKS) — Grim Reaper Academy

A troll-but-useful Streamlit study app for YKS prep:
- **Countdown Timer** (minute input → second-by-second countdown)
- **Daily progressive minutes** (gets harder every day )
- **AI Study Coach** (topic + time → strict plan + mini questions)
- **EN/TR language toggle**
- **Alarm sound** (plays an MP3 at the end)

> Motto: **You had time. You wasted it.**

---

##  Features

### Countdown Timer
- Enter minutes → app counts down **second by second**
- End of timer → plays `breadfan.mp3` (starting at 52s)

### Daily Progressive Difficulty
- First run creates `data.json`
- Each day increases the suggested minutes:
  - Day 1: 1 min
  - Day 2: 2 min
  - Day 3: 3 min
  - ...and so on

### AI Study Plan Generator
- Input: **Topic** + **Time (minutes)**
- Output:
  - Time-boxed plan (does not exceed time)
  - Short YKS-focused summary
  - 3 mini test questions
- No motivational fluff. Just work.

###  Language Switch (EN/TR)
- UI can toggle between English and Turkish

---

## Project Structure (recommended)

