example = {
    "Time": 71530,
    "Distance": 940200
    }

input = {
    "Time": 48989083,
    "Distance": 390110311121360
    }

data = input
race_time = data['Time']
record_distance = data['Distance']
counter = 0


def calculate_counter(record_distance, race_time):

    j_start = int((2 * record_distance / race_time) ** 0.5)

    # Inicializar el contador
    counter = 0

    # Iterar desde j_start hasta race_time
    for speed in range(j_start, race_time + 1):
        time_left = race_time - speed
        distance_made = time_left * speed
        if distance_made > record_distance:
            # Incrementar el contador si la distancia hecha es mayor que el record
            counter += 1

    return counter





print(calculate_counter(record_distance, race_time))

