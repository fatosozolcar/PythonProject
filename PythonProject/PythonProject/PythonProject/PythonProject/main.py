import time

def countdown(t):
    while t>0:
        print(t)
        t -= 1
        time.sleep(1)
    print('Goodbye')



print("kaçtan geriye doğru saymak istiyorsunuz:")
seconds = input()
while not seconds.isdigit():
    print("That wasn't an integer! Enter an integer")
    seconds = input()
seconds = int(seconds)
countdown(seconds)