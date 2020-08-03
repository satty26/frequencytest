#Check the frequency you last heard and confirm your ears are all good or you need to see your doctor :)
import winsound
for i in range(10000,20000,100):
    frequency = i
    print("Currently hearing frequency", i);
    duration = 200
    winsound.Beep(frequency, duration)
    continue;
