import winsound
for i in range(10000,20000,100):
    frequency = i
    print("Currently hearing frequency", i);
    duration = 200
    winsound.Beep(frequency, duration)
    continue;