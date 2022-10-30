import matplotlib.pyplot as plt
import random

values_x_1 = [random.randint(1,10) for i in range(0,10)]
values_y_1 = [random.randint(1,10) for i in range(0,10)]
values_x_2 = [0,1,2,3,4,5,6,7,8,9]
values_y_2 = [random.randint(1,10) for i in range(0,10)]


fig = plt.figure()
plt.scatter(values_x_1, values_y_1)
plt.plot(values_x_2, values_y_2)
fig.suptitle('Random Plot', fontsize=8)
plt.savefig("test.png")
plt.show()


