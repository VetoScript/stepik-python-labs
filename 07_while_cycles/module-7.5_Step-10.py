hour1 = int(input())
minute1 = int(input())
hour2 = int(input())
minute2 = int(input())
start_minutes = hour1 * 60 + minute1
end_minutes = hour2 * 60 + minute2
while start_minutes <= end_minutes:
    h = start_minutes // 60
    m = start_minutes % 60
    start_minutes += 1
    print(f"{h:02}:{m:02}")
