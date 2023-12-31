# Program that performs physics calculations for different trip scenarios

def trip_physics(speed_kmh=None, distance_km=None, time=None, stop_time=None):
    if time is None:
        if distance_km is not None and speed_kmh is not None:
            time = distance_km / speed_kmh
            print(f'If I drive at {speed_kmh} km/h, I will need {time} hours to cover {distance_km} km.')
        else:
            print('Cannot calculate time without distance and speed information.')
    elif time < 1: # Minutes scope
        time_minutes = round(time * 60) # Convert time to minutes
        if not stop_time: # Equivalent to if stop_time is None:
            if speed_kmh is None:
                speed_kmh = round(distance_km / time)
                print(f'In order to drive {distance_km} km in {time_minutes} minutes without stopping, I need to be at a speed of {speed_kmh} km/h.')
            elif distance_km is None:
                distance_km = speed_kmh * time
                print(f'Assuming that I will drive at {speed_kmh} km/h during {time_minutes} minutes, I will travel a total distance of {distance_km} km.')
        else:
            if stop_time < 1:
                stop_time_minutes = stop_time*60
                # if I want to be there on time (urgent case)
                if stop_time_minutes < time_minutes:
                    total_minutes_left = time_minutes - stop_time_minutes
                    if speed_kmh is None:
                        speed_kmh = round(distance_km /(total_minutes_left/60))
                        print(f'Well, to be there on time, I will need to drive at {speed_kmh} km/h to travel {distance_km} km in {total_minutes_left} minutes, assuming that I will make a stop of {stop_time_minutes} minutes.')
                    elif distance_km is None:
                        distance_km = speed_kmh * (total_minutes_left/60)
                        print(f'With my {stop_time_minutes}-minute stop during the trip, I will be able to travel {distance_km} km... Assuming that I will drive at {speed_kmh} km/h for {time_minutes} minutes.')
                else:
                    total_minutes_plus = time_minutes + stop_time_minutes
                    if speed_kmh is None:
                        speed_kmh = round(distance_km / (total_minutes_plus/60))
                        print(f'Since my stop during the trip will be = or > than the trip duration ({stop_time_minutes} mins vs {time_minutes} mins), I will drive at {speed_kmh} km/h for {distance_km} km, since the total time of the trip is {total_minutes_plus} minutes.')
                    elif distance_km is None:
                        distance_km = speed_kmh * (total_minutes_plus/60)
                        print(f'Because I need to stop for {stop_time_minutes} minutes, I will be able to travel {distance_km} km, assuming that my speed is {speed_kmh} km/h during {total_minutes_plus} minutes.')
    else: # Hours scope
        if not stop_time:
            if speed_kmh is None:
                    speed_kmh = round(distance_km / time)
                    print(f'In order to drive {distance_km} km in {time} hour(s) without stopping, I need to be at a speed of {speed_kmh} km/h.')
            elif distance_km is None:
                distance_km = speed_kmh * time
                print(f'Assuming that I will drive at {speed_kmh} km/h during {time} hour(s), I will travel a total distance of {distance_km} km.')
        else:
            if stop_time < 1:
                stop_time_minutes = stop_time*60
                total_hours_left = time - stop_time # Ex: 2h trip with a break of 0.5 hours (need to do a trip in 1,5h)
                if speed_kmh is None:
                    speed_kmh = round(distance_km / total_hours_left)
                    print(f'Well, to be there on time, I will need to drive at {speed_kmh} km/h to travel {distance_km} km in {total_hours_left} hour(s).')
                elif distance_km is None:
                    distance_km = speed_kmh * total_hours_left
                    print(f'With my {stop_time_minutes}-minute stop during the trip, I will be able to travel {distance_km} km... Assuming that I will drive at {speed_kmh} km/h for {time} hour(s)')
            else:
                if stop_time > time:
                    total_hours_plus = time + stop_time
                    if speed_kmh is None:
                        speed_kmh = round(distance_km / total_hours_plus)
                        print(f'Since my stop during the trip will be = or > than the trip duration ({stop_time} hour(s) vs {time} hour(s)), I will drive at {speed_kmh} km/h for {distance_km} km, since the total time of the trip is {total_hours_plus} hour(s).')
                    if distance_km is None:
                        distance_km = speed_kmh * total_hours_plus
                        print(f'Because I need to stop for {stop_time} hour(s), I will be able to travel {distance_km} km, assuming that my speed is {speed_kmh} km/h during {total_hours_plus} minutes.')



'''
---> WRITE YOUR TRIP AND SEE THE RESULTS <----
trip1 = trip_physics()
trip1
'''