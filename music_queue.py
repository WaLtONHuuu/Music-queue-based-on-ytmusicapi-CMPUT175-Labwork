

# Import time format change function from utils.py, import Song class from song.py, create MusicQueue class
# Author: Chen Hu
# When: May 22, 2026


from song import Song
from utils import seconds_to_time_format

class MusicQueue:
    def __init__(self):
        """
        Input: None
        Returns: None
        Working: initializes the queue to be empty
        """
        self.items = []
        self.length = 0

    def enqueue_b(self, item: Song):
        '''
        Input: the element to be enqueued
        Returns: None
        Working: enqueues the Song object to the back of the queue
        '''
        self.items.append(item)
        self.length += item.get_duration()

    def enqueue_f(self, item: Song):  # enqueue_f (add to the strat of the queue) method
        '''
        Input: element to be enqueued
        Returns: None
        Working: enqueues the Song object to the front of the queue
        '''
        # TODO: Implement this function
        self.items.insert(0, item)
        self.length += item.get_duration()

    def dequeue(self):  # dequeue (pop the end of the queue) method
        '''
        Input: None
        Returns: object that was dequeued
        Working: dequeues the Song from the top of the queue and return it
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
        Returns: front-most item in the queue
        Working: returns the front-most item in the queue, and DOES NOT change the queue if queue is empty it should
        raise an exception
        """
        if self.is_empty():
            raise IndexError("Invalid peek: empty queue")
        return self.items[0]

    def is_empty(self):  # check if the queue if empty method
        """
        Input: None
        Returns: True if the queue is empty, False otherwise
        """
        return len(self.items) == 0

    def size(self):  # get to know the size of the queue method
        """
        Input: None
        Returns: number of items in the queue
        """
        return len(self.items)

    def clear(self):  # delete elements in queue method
        """
        Input: None
        Returns: None
        Working: removes all items from the queue, and sets the size to 0
        clear() should not change the capacity
        """
        self.items = []
        self.length = 0

    def __str__(self):
        """
        Input: None
        Returns: A string representation of the queue
        Working: returns a string representation of the queue
        """
        str_exp = f"\nQUEUE LENGTH: {seconds_to_time_format(self.length)}\nSONGS QUEUED: {self.size()}\n"
        for i in range(len(self.items)):
            str_exp += f"{i + 1}. {self.items[i]}\n"
        return str_exp.strip('\n')