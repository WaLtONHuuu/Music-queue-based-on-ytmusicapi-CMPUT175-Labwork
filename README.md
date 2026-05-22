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
