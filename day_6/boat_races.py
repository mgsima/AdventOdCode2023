example = {
    "Time": [7,  15,   30],
    "Distance":  [9,  40,  200]
}

input = {
    "Time": [48, 98, 90, 83],
    "Distance": [390, 1103, 1112, 1360]}

data = input
time = data['Time']
distance = data['Distance']

result = 1
sum_of_wins = []

for i in range(len(time)):
    race_time = time[i]
    record_distance = distance[i]
    counter = 0

    for j in range(race_time+1):
        time_left = race_time-j
        speed = j
        distance_made = time_left*speed
        if distance_made > record_distance:
            print(f"time left: {race_time-j}; speed: {j}; distance: {(race_time-j)*j}")
            counter+=1
    sum_of_wins.append(counter)

for i in sum_of_wins:
    result*=i

print(result)

