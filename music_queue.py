# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 5 - Music Queue
#
# ~ Created by CMPUT 175 Team ~
# =================================================================

# Install ytmusicapi using pip or pip3
from ytmusicapi import YTMusic
from structures import MusicQueue, Song, time_to_seconds
import os

NO_OF_RESULTS = 5

def clear():  # PROVIDED clear function
    """
    Input: None
    Returns: None
    Working:
    This function clears terminal screen
    """
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')

def extract_artists(song_info):  # extract artists function
    """
    Input: Data of the song as originally retrieved (dictionary format)
    Returns: All artists involved in the song as a string or "NA" if no artist info is available.
    Working:
    This function makes sure that all artists involved in a song show up in the final 
    representation.
    """
    # TODO: Implement this function
    if song_info["artists"] != None:
        artists=song_info["artists"]
    else:
        artists=None
    names=[]
    if artists != None:
        for name in artists:
            names.append(name["name"])
        return ", ".join(names)
    else:
        return "NA"

def song_search(query):  # song search function
    """
    Input: Search query
    Returns: Top 5 results from the retrieved data
    Working:
    This function invokes the search method on YTMusic object with required arguments
    and returns the top "NO_OF_RESULTS" results.
    """
    # TODO: Implement this function
    ytmusic = YTMusic()
    results = ytmusic.search(query, filter="songs")
    return results[0:NO_OF_RESULTS]


def filter_info(results):  # filter info function
    """
    Input: Search results in a JSON like format
    Returns: List of Song Objects
    Working:
    This function is supposed to extract the required information from the JSON,
    create Song objects and append them to a list. If an error occurs, raise an
    exception.
    """
    # TODO: Implement this function
    songs=[]
    try:
        for result in results:
            title=result["title"]
            artists=extract_artists(result)
            duration_seconds=time_to_seconds(result["duration"])
            song = Song(title, artists, duration_seconds)
            songs.append(song)
    except Exception:
        raise Exception("Invalid song info")
    return songs

def print_song_results(results):  # PROVIDED print song result function
    """
    Input: List containing "Song" objects
    Returns: None
    Working:
    This function is reponsible for printing the song results with a serial number beside them.
    """
    assert type(results[0]) == Song, "The list to be printed doesn't have the items of type 'Song'"

    print("RESULTS:")
    for i in range(len(results)):
        print(f"{i+1}. {results[i]}")

def search():  # search function
    """
    Input: None
    Return: A Song object representing the song the user wants to add into the Queue, or None if the user wants to go back
    Working:
    1. This function takes search query from the user
    2. Searches for the song using songSearch function
    3. Filters the information using filterInfo function
    4. Prints the song results using printSongResults function
    5. Asks for user choice
    6. Returns the chosen song information
    7. If the user wants to go back, it returns None
    """
    # TODO: Implement this function
    clear()
    repeat=True
    while repeat:
        query=input("Search: ")
        results=song_search(query)
        songs=filter_info(results)
        print_song_results(songs)
        print("\nChoose on e of the following options:\n"
              "        Enter a number (1-5) to add a song to playlist\n"
              "        Enter '0' to search again\n"
              "        Enter 'q' to go back")
        correct = True
        while correct:
            chosen=input(">> ").strip()
            if chosen=="q":
                repeat=False
                return None
            if chosen=="0":
                clear()
                repeat=True
                correct=False
            elif chosen.isdigit():
                num=int(chosen)
                if 1<=num<=len(songs):
                    repeat = False
                    return songs[num-1]
                else:
                    print("Invalid Input")
                    correct=True
            else:
                print("Invalid Input")
                correct=True

def main():  # PROVIDED main function
    """
    Drive Function
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
                print('  ',queue.peek(),'\n')
            else: 
                print('  ',"None",'\n')

            print(choice_str)
            choice = input('>> ')
            while choice not in ['1','2','3','4','5']:
                print('Invalid Input.')
                choice = input('>> ')
            
            if choice == '1':
                song = search()
                if song != None:
                    if queue.is_empty():
                        queue.enqueue_b(song)
                    else:
                        place = input("Where would you like to add the song:\n\t1. Top\n\t2. End\n>> ")
                        while place not in ['1','2']:
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
                queue.dequeue()
                print('Now playing:')
                if queue.size() > 0:
                    print("  ",queue.peek())
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