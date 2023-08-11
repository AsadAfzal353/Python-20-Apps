# Importing required libraries
import queue
import threading

# Defining required functions
def increment(first_cue, second_cue, num_iters, A):
    """This function multiplies two arguments and then
    increments the output for num_iters times.
    1st Cue: Value is retrived and operations are performed
    2nd Cue: Output is stored in it"""
    for _ in range(num_iters):
        out = (A*first_cue.get()) + 1
        print("Performed Increment!")
        second_cue.put(out)

def square(first_cue, second_cue, num_iters, A):
    """This function multiplies two arguments and then
    squares the output for num_iters times.
    1st Cue: Output is stored in it
    2nd Cue: Value is retrived and operations are performed"""
    for _ in range(num_iters):
        out = (A*second_cue.get())**2
        print("Performed Square!")
        first_cue.put(out)

if __name__ == "__main__":
    # Defining required variables
    A = 2
    B = 6

    # Inputting the number of iterations required
    Z = int(input("Enter the number of iterations: "))

    # Initialzing two queues and inserting B into 1st queue
    first_cue = queue.Queue()
    second_cue = queue.Queue()
    first_cue.put(B)

    # Creating two threads for the functions
    t1 = threading.Thread(target=increment, args=(first_cue, second_cue, Z, A))
    t2 = threading.Thread(target=square, args=(first_cue, second_cue, Z, A))

    # Starting the threads
    t1.start()
    t2.start()

    # Joining the threads
    t1.join()
    t2.join()

    # Outputting the results
    print(first_cue.get())
    print("Done!")  