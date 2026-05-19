# =================================================================
# CMPUT 175 - Introduction to the Foundations of Computation II
# Lab 5 - Music Queue
#
# ~ Created by CMPUT 175 Team ~
# ~ Modified by Chen Hu ~
# =================================================================

def time_to_seconds(time_str):
    """
    Input: A string representing time in the format "hh:mm:ss"
    Returns: Total seconds in the time string
    Working:
    This function converts the time string into total seconds.
    """
    parts = time_str.split(":")
    
    if len(parts) == 3:
        hours, minutes, seconds = map(int, parts)
    elif len(parts) == 2:
        minutes, seconds = map(int, parts)
        hours = 0
    else:
        raise ValueError("Invalid time format")

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def seconds_to_time_format(seconds):
    """
    Input: Total seconds
    Returns: Time string in the format "hh:mm:ss"
    Working:
    This function converts the total seconds into a time string.
    """
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if hours > 0:
        return f"{hours}:{minutes:02}:{seconds:02}"
    else:
        return f"{minutes}:{seconds:02}"


class Song:
    def __init__(self, name, artist, dur):
        """
        Input: Name of the song, Artist of the song, Duration of the song
        Returns: None
        Working:
        This function initializes the Song object with the name, artist, and duration
        """
        assert type(name) == str
        assert type(artist) == str
        assert type(dur) == int

        self.name = name
        self.artist = artist
        self.duration = dur

    def get_name(self):
        """
        Input: None
        Returns: Name of the song
        """
        return self.name

    def get_artist(self):
        """
        Input: None
        Returns: Artist of the song
        """
        return self.artist

    def get_duration(self):
        """
        Input: None
        Returns: Duration of the song
        """
        return self.duration
    
    def __str__(self):
        """
        Input: None
        Returns: String representation of the song
        """
        return f"{self.name}\n   Artists: {self.artist}\n   Duration: {seconds_to_time_format(self.duration)}"


class MusicQueue: 
    def __init__(self): 
        """
        Input: None
        Returns: None
        Working:
        This function initializes the queue to be empty
        """
        self.items = []
        self.length = 0

    def enqueue_b(self, item: Song):  # enqueue_b (add to the end of the queue) method
        '''
        Input: the element to be enqueued
        Returns: None
        Working:
        This function nqueues the Song object to the back of the queue
        '''
        self.items.append(item)
        self.length += item.get_duration()

    def enqueue_f(self, item: Song):  # enqueue_f (add to the strat of the queue) method
        '''
        Input: the element to be enqueued
        Returns: None
        Working:
        This function enqueues the Song object to the front of the queue
        '''
        self.items.insert(0,item)
        self.length += item.get_duration()
            
    def dequeue(self):  # dequeue (pop the end of the queue) method
        '''
        Input: None
        Returns: The object that was dequeued
        Working:
        This function dequeues the Song from the top of the queue and return it
        if queue is empty it should raise an exception
        '''
        if self.is_empty():
            raise IndexError("Error: Queue is empty")
        removed_element = self.items.pop(0)
        self.length -= removed_element.get_duration()
        return removed_element
          
    def peek(self):  # peek (get to know the end of the queue) method
        """
        Input: None
        Returns: The front-most item in the queue
        Working:
        This function returns the front-most item in the queue, and DOES NOT change the queue.
        if queue is empty it should raise an exception
        """
        if self.is_empty():
            raise IndexError("Invalid peek: empty queue")
        return self.items[0]
           
    def is_empty(self):  # check if the queue if empty method
        """
        Input: None
        Returns: True if the queue is empty, False otherwise
        """
        return len(self.items)==0
            
    def size(self):  # get to know the size of the queue method
        """
        Input: None
        Returns: The number of items in the queue
        """        
        return len(self.items)
           
    def clear(self):  # delete elements in queue method
        """
        Input: None
        Returns: None
        Working:
        This function removes all items from the queue, and sets the size to 0    
        clear() should not change the capacity 
        """
        self.items=[]
        self.length=0

    def __str__(self):               
        """
        Input: None
        Returns: A string representation of the queue
        Working:
        This function returns a string representation of the queue
        """
        str_exp = f"\nQUEUE LENGTH: {seconds_to_time_format(self.length)}\nSONGS QUEUED: {self.size()}\n"  
        for i in range(len(self.items)):
            str_exp += f"{i+1}. {self.items[i]}\n"
        return str_exp.strip('\n')
    

# ------------------------- Test Cases -------------------------

def main():
    """
    Driver Function
    """
    print(f"\n{'='*5} Running Test Cases for MusicQueue {'='*4}\n")

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

    print(f"\n{'='*15} Music Queue {'='*16}\n")
    print(q)

    first_song = q.dequeue()
    assert first_song.get_name() == "I Want It That Way", "Test Failed: Dequeue"
    assert q.size() == 4, "Test Failed: Dequeue Size Update"

    second_song = q.dequeue()
    assert second_song.get_name() == "Open Hearts", "Test Failed: Dequeue"
    assert q.size() == 3, "Test Failed: Dequeue Size Update"

    print(f"\n{'='*11} Queue after Dequeuing {'='*11}\n")
    print(q)

    q.clear()
    assert q.is_empty(), "Test Failed: Clear"

    print("\nAll tests passed successfully!\n")

if __name__ == "__main__":
    main()
