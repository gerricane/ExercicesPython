import time
# for i in range (25):
#     time.sleep(1)
#     print(".", end="", flush=True)


d_coque = 180
min = d_coque // 60
sec = d_coque - min * 60

while not d_coque == 0:
    print(f"Temps restant: {min:02d}:{sec:02d} minutes",end="")
    for i in range (10):
        time.sleep(1)
        print(".", end="", flush=True)
        d_coque -= 1
        min = d_coque // 60
        sec = d_coque - min * 60
    print()