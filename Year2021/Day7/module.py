from multiprocessing import Process, Queue

f = open("Year2021/Day7/data")

lines = f.read()
dataStr = lines.split(",")
data = []
for i in dataStr:
    data.append(int(i))


def method1():
    fuel = []
    for i in range(500):
        fuelConsumption = 0
        for j in data:
            fuelConsumption += abs(i - j)
        fuel.append((i, fuelConsumption))
    q1.put(fuel)


def method2():
    fuel2 = []
    for i in range(500):
        fuelConsumption2 = 0
        for j in data:
            for h in range(abs(i - j)):
                fuelConsumption2 += (h + 1)

        fuel2.append((i, fuelConsumption2))
    q2.put(fuel2)

q1 = Queue()
q2 = Queue()
p1 = Process(target=method1)
p2 = Process(target=method2)
p1.start()
p2.start()
fuel = q1.get()
fuel.sort(key=lambda y: y[1])
print("{} fuel needed to move to {}".format(fuel[0][1], fuel[0][0]))
fuel2 = q2.get()
fuel2.sort(key=lambda y: y[1])
print("{} fuel needed to move to {} using alternate method".format(fuel2[0][1], fuel2[0][0]))
p1.join()
p2.join()
