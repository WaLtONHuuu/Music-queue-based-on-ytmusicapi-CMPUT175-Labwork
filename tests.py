

# Import time format change function from utils.py, import Song class from song.py, import MusicQueue class from
# music_queue.py; testing: time format change function, MusicQueue class
# Author: Chen Hu
# When: May 22, 2026


from song import Song
from music_queue import MusicQueue
from utils import time_to_seconds


def test_time_to_seconds():
    assert time_to_seconds("3:33") == 213
    assert time_to_seconds("1:02:03") == 3723

def test_MusicQueue_class():
    print(f"\n{'=' * 5} Running Test Cases for MusicQueue {'=' * 4}\n")

    q = MusicQueue()

    song1 = Song("I Want It That Way", "Backstreet Boys", time_to_seconds("3:33"))
    song2 = Song("Baby Shark", "CoComelon", time_to_seconds("2:24"))
    song3 = Song("The Time Is Now", "John Cena", time_to_seconds("2:56"))
    song4 = Song("Open Hearts", "The Weeknd", time_to_seconds("3:55"))
    song5 = Song("Taste", "Sabrina Carpenter", time_to_seconds("2:37"))

    q.enqueue_b(song4)
    assert q.size() == 1, "Test Failed: EnqueueB"

    q.enqueue_b(song2)
    assert q.size() == 2, "Test Failed: EnqueueB"

    q.enqueue_f(song1)
    assert q.size() == 3, "Test Failed: EnqueueF"

    assert q.peek().get_name() == "I Want It That Way", "Test Failed: Peek"

    q.enqueue_b(song3)
    assert q.size() == 4, "Test Failed: EnqueueB"

    q.enqueue_b(song5)
    assert q.size() == 5, "Test Failed: EnqueueB"

    print(f"\n{'=' * 15} Music Queue {'=' * 16}\n")
    print(q)

    first_song = q.dequeue()
    assert first_song.get_name() == "I Want It That Way", "Test Failed: Dequeue"
    assert q.size() == 4, "Test Failed: Dequeue Size Update"

    second_song = q.dequeue()
    assert second_song.get_name() == "Open Hearts", "Test Failed: Dequeue"
    assert q.size() == 3, "Test Failed: Dequeue Size Update"

    print(f"\n{'=' * 11} Queue after Dequeuing {'=' * 11}\n")
    print(q)

    q.clear()
    assert q.is_empty(), "Test Failed: Clear"

def main():
    test_time_to_seconds()
    test_MusicQueue_class()

    print("\nAll tests passed successfully!\n")

if __name__ == "__main__":
    main()