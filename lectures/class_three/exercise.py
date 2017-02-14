GOAL_NUMBER_OF_STEPS = 10000
ACTUAL_NUMBER_OF_STEPS = int(input("Number of steps you walked today?"))
while ACTUAL_NUMBER_OF_STEPS < 0:
    print("You entered a number less than 0, steps can only be positive, fool")
    ACTUAL_NUMBER_OF_STEPS = int(input("Number of steps you walked today?"))
print(ACTUAL_NUMBER_OF_STEPS)

print("we walked:")
print(abs(GOAL_NUMBER_OF_STEPS - ACTUAL_NUMBER_OF_STEPS))
if GOAL_NUMBER_OF_STEPS - ACTUAL_NUMBER_OF_STEPS > 0:
    print("fewer than our goal")
else:
    print("more than our goal")
