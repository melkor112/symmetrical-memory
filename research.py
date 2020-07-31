
res_perc = 0.0
time = 0
base = 85      # Base Cost
bonus = 0.13    # Research Speed Bonus
aot = 1.54      # Ahead-of-time penalty (not years ahead)
base /= 1+bonus
while res_perc<1:
   res_perc += 1/base/(1+aot)
   aot -= 2/365
   if aot<0: aot = 0
   time += 1
print(time)     # Prints total time needed