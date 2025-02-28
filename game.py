import random
import time

start_time = time.time()
fuck = int(input("How many seconds do you want to play?: "))
timeout = fuck


choice = random.randint(1, 3000)

while True:
    x = int(input("Chosse a podsitive integer between (1, 3000): "))
    if time.time() - start_time > timeout:
        print("Timeout")
        break
    elif x < 1 or x > 3000:
        print("Invalid number")
        continue
    elif x > choice:
        print("Too high")
        continue
    elif x < choice:
        print("Too low")
        continue
    elif x == choice:
        print("You won")
        break
