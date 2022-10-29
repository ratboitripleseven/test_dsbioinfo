import matplotlib.pyplot as plt
import random

values_x = [random.randint(1,10) for i in range(0,10)]
values_y = [random.randint(1,10) for i in range(0,10)]
plt.scatter(values_x, values_y)
plt.savefig("test.png")
plt.show()


