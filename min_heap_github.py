from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        This method adds a new object to the MinHeap maintaining heap property.
        """
        self.heap.append(node)
        node_index = self.heap.length() - 1  # Put new element at the end of the array
        parent_index = ((node_index - 1) // 2)  # Create parent index

        # Compare the value of the inserted element with the value of its parent
        # while (self.heap.get_at_index(parent_index) > self.heap.get_at_index(node_index)) and node_index > 0:
        while (parent_index >= 0 and self.heap.get_at_index(node_index) < self.heap.get_at_index(parent_index)):
            # If the value of the parent is greater than the value of the inserted element,
            self.heap.swap(node_index, parent_index)  # swap the elements in the array and repeat from step 2.
            node_index = parent_index
            parent_index = ((node_index - 1) // 2)
        else:
            return  # if the node is in the correct place, return to exit

    def get_min(self) -> object:
        """
        This method returns an object with a minimum key without
        removing it from the heap. If the heap is empty, the method
        raises a MinHeapException.
        """
        if self.heap.length() == 0:
            raise MinHeapException
        else:
            return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        This method returns an object with a minimum key and removes it
        from the heap. If the heap is empty, the method raises a
        MinHeapException.
        """

        if self.is_empty():
            raise MinHeapException

        min_value = self.heap.get_at_index(0)  # get element of first value in array (for later)

        # Replace the value of the first element in the array with the value of the last element
        self.heap.swap(0, self.heap.length() - 1)
        self.heap.pop()  # and remove the last element

        replacement_index = 0  # set replacement as initial 0

        while True:
            if self.is_empty():
                break

            child1_index = 2 * replacement_index + 1  # (2 * i + 1) left leaf
            child2_index = 2 * replacement_index + 2  # (2 * i + 2) right leaf

            # If the array is not empty (i.e., it started with more than one element),
            # If both of these elements fall beyond the bounds of the array, we can stop here.
            if child1_index >= self.heap.length():
                break

            # Compare the value of the replacement element with the minimum value of its two children
            min_child_index = child1_index
            if child2_index < self.heap.length():
                if (self.heap.get_at_index(child2_index) < self.heap.get_at_index(child1_index)):
                    min_child_index = child2_index

            # If the replacement element’s value is less than its minimum child’s value,
            # swap those two elements in the array and repeat from step 3.
            if (self.heap.get_at_index(replacement_index) > self.heap.get_at_index(min_child_index)):
                self.heap.swap(replacement_index, min_child_index)
                replacement_index = min_child_index

            else:
                break

        return min_value


    def build_heap(self, da: DynamicArray) -> None:
        """
        This method receives a dynamic array with objects in any order
        and builds a proper MinHeap from them. Current content of the
        MinHeap is lost.
        """

        self.heap = DynamicArray()
        # current_index = da.length() // 2 - 1  # Grab index of last non-leaf element in heap
        # child1_index = 2 * current_index + 1  # left leaf
        # child2_index = 2 * current_index + 2  # right leaf

        for i in range(da.length()):
            self.add(da.get_at_index(i)) #use adds percolate
        return




# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())
    #
    #
    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")

    da2 = DynamicArray([100, 20, 6, 200, 90, 150, 300, 1, 50, 350, 250])
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    #print(da)
    da.set_at_index(0, 500)
    print(da)
    print(h)
    # h.build_heap(da2)
    # print(da2)
    # print(h)
