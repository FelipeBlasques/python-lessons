# while - continue

count = 0

while count < 20:
    count += 1

    if count <= 6 and count >= 3:
        print(f"Where's {count}?")
        continue
        

    print(count)

    if count == 10:
        break

print('End')
