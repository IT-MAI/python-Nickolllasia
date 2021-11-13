def time(n):
    d=n//1440
    h=n//60-24*d
    m=n-h*60-d*1440
    print(f"Время {h}:{m}")
time(5280)
