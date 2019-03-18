import threading, queue
import time

def washer(dishes, output):
    for dish in dishes:
        print('Washing', dish, 'dish')
        time.sleep(5)
        output.put(dish)

def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print('Drying', dish, 'dish')
        time.sleep(10)
        dish_queue.task_done()

dish_queue = queue.Queue()
for n in range(2):
    dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
    dryer_thread.start()

dishes = ['salad', 'bread', 'entree', 'dessert']
washer(dishes, dish_queue)
dish_queue.join()

