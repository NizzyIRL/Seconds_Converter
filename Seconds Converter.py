str_seconds = input("Number of seconds you wish to convert: ")
total_secs = int(str_seconds)

hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
mins =  secs_still_remaining // 60
secs_final = secs_still_remaining  % 60

print("Hrs=", hours, "mins=", mins, "secs=", secs_final)