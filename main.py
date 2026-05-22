

# Main program for the Music Queue project, handles user input
# Author: Chen Hu
# When: May 22, 2026


from song import Song
from music_queue import MusicQueue

from utils import clear

from youtube_search import song_search, filter_info


def print_song_results(results):
    """
    Input: List containing "Song" objects
    Returns: None
    Working:
    This function is reponsible for printing the song results with a serial number beside them.
    """
    assert type(results[0]) == Song, "The list to be printed doesn't have the items of type 'Song'"

    print("RESULTS:")
    for i in range(len(results)):
        print(f"{i + 1}. {results[i]}")


def search():
    """
    Input: None
    Return: Song object of the song the user wants to add into the Queue, or None if the user wants to go back
    Working: search song, filters information, print results, ask for choice, return chosen information,
    returns None if the user go back
    """
    clear()
    repeat = True
    while repeat:
        query = input("Search: ")
        results = song_search(query)
        songs = filter_info(results)
        print_song_results(songs)
        print("\nChoose on e of the following options:\n"
              "        Enter a number (1-5) to add a song to playlist\n"
              "        Enter '0' to search again\n"
              "        Enter 'q' to go back")
        correct = True
        while correct:
            chosen = input(">> ").strip()
            if chosen == "q":
                return None
            if chosen == "0":
                clear()
                repeat = True
                correct = False
            elif chosen.isdigit():
                num = int(chosen)
                if 1 <= num <= len(songs):
                    return songs[num - 1]
                else:
                    print("Invalid Input")
                    correct = True
            else:
                print("Invalid Input")
                correct = True


def main():
    """
    MAIN Function
    """
    queue = MusicQueue()
    clear()
    print("WELCOME\n")
    choice_str = """Choose one of the following options:
                    \t1. Add Song
                    \t2. Next Song
                    \t3. Show Queue
                    \t4. Clear Queue
                    \t5. Quit
                    \tEnter the choice (eg: 2)
                """
    contBuild = True
    try:
        while contBuild:

            print('Currently playing:')
            if queue.is_empty() == False:
                print('  ', queue.peek(), '\n')
            else:
                print('  ', "None", '\n')

            print(choice_str)
            choice = input('>> ')
            while choice not in ['1', '2', '3', '4', '5']:
                print('Invalid Input.')
                choice = input('>> ')

            if choice == '1':
                song = search()
                if song != None:
                    if queue.is_empty():
                        queue.enqueue_b(song)
                    else:
                        place = input("Where would you like to add the song:\n\t1. Top\n\t2. End\n>> ")
                        while place not in ['1', '2']:
                            print('Invalid Input.')
                            place = input('>> ')

                        if place == '1':
                            queue.enqueue_f(song)
                        elif place == '2':
                            queue.enqueue_b(song)
                    print("Song added successfully!")
                    input("\nPress enter key to continue...")

            elif choice == '2':
                clear()
                if queue.is_empty():
                    print("Queue is empty. No next song to play.")
                else:
                    queue.dequeue()
                    print('Now playing:')
                    if queue.size() > 0:
                        print("  ", queue.peek())
                    else:
                        print("   None")
                input("\nPress enter key to continue...")

            elif choice == '3':
                clear()
                try:
                    print(queue)
                    input("\nPress enter key to continue...")
                except Exception as e:
                    print(e)

            elif choice == '4':
                clear()
                queue.clear()
                print('The queue has been cleared!')
                input("\nPress enter key to continue...")

            elif choice == '5':
                contBuild = False

            clear()

    except Exception as e:
        print(e)

    print("Thanks for listening!")


if __name__ == "__main__":
    main()