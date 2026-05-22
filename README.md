<p align="center">
    <h1 align="center">Music Queue</h1>
    <h5 align="center">A multifunctional music queue Python script based on ytmusicapi.</h5>
    <h6 align="center">UofA CMPUT 175 Labwork · Project Optimization & Refactoring</h6>
    <h6 align="center">FIRST YEAR STUDENT WORK</h6>
</p>

---

## Overview

**Music Queue** is a command-line Python application that allows users to search for songs, add them to a queue, play the next song, view the current queue, and clear the queue.

This project was originally created as part of CMPUT 175 labwork and later refactored into a cleaner, more modular project structure.

---

## Features

- Search songs using `ytmusicapi`
- Add songs to the front or end of the queue
- View the currently playing song
- Show all songs in the queue
- Play the next song
- Clear the entire queue
- Convert song duration between seconds and time format
- Run basic tests for core queue functions

---

## Project Structure

```text
music-queue-refactor/
├── main.py             # Main program and user interaction
├── music_queue.py      # MusicQueue class
├── song.py             # Song class
├── youtube_search.py   # YouTube Music search and result filtering
├── utils.py            # Helper functions
├── tests.py            # Basic tests
├── requirements.txt    # Required Python package
└── README.md           # Project documentation

## Requirements

This project requires **Python 3** and the following Python package:

```text
ytmusicapi
```

The required package is listed in `requirements.txt`.

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

If your Mac uses `python3` and `pip3`, you can also run:

```bash
pip3 install -r requirements.txt
```

---

## requirements.txt

The `requirements.txt` file should contain:

```text
ytmusicapi
```

This file is used by `pip` to install the external package needed for this project.

---

## How to Run

Run the main program:

```bash
python3 main.py
```

Then follow the menu options in the terminal.

---

## How to Test

Run the test file:

```bash
python3 tests.py
```

If all tests pass, you should see:

```text
All tests passed successfully!
```

---

## File Responsibilities

### `main.py`

Controls the main program flow, user input, menu options, and interaction between different modules.

### `song.py`

Contains the `Song` class, which stores song name, artist, and duration.

### `music_queue.py`

Contains the `MusicQueue` class, which manages queue operations such as adding songs, playing the next song, checking the current song, and clearing the queue.

### `youtube_search.py`

Handles YouTube Music search logic using `ytmusicapi`, extracts useful song information, and converts search results into `Song` objects.

### `utils.py`

Contains helper functions such as time conversion and clearing the terminal screen.

### `tests.py`

Contains basic tests for the time conversion function and the `MusicQueue` class.

---

## Refactoring Notes

The original lab version placed most of the program logic in a small number of files.

This refactored version separates responsibilities into different modules:

- `song.py` handles the `Song` object
- `music_queue.py` handles queue operations
- `youtube_search.py` handles song search and data filtering
- `utils.py` handles helper functions such as time conversion and screen clearing
- `main.py` handles user input and program flow
- `tests.py` checks the core functionality

The goal of this refactor was to make the project easier to read, test, maintain, and extend.

---

## Author

**Chen Hu**  
First-year Computer Science student  
University of Alberta

---

## Note

This project is based on CMPUT 175 coursework and was refactored for learning and portfolio-building purposes.
