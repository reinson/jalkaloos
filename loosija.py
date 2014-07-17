
import random


def loosi_tiimid(mangijad,dict):
    random.shuffle(mangijad)
    mangijad2 = sorted(mangijad, key = dict.get, reverse = True)
    
    if "tauri" in mangijad2:
        tauri = True

    #print mangijad2
    tiimid = [[],[]]
    tiimid[0] = [mangijad2.pop(0)]
    tiimid[1] = [mangijad2.pop(0)]


    if tauri:
        next = 1
        for i in mangijad2:
            tiimid[next].append(i)
            next = (next + 1) % 2

    else:
    
        if (len(mangijad2) + 2) % 4 == 1:
            next = 0
        else:
            next = 1

        previous = next

        for i in mangijad2:
            tiimid[next].append(i)
            if next == previous:
                next = (next + 1) % 2
            else:
                previous = next
            print tiimid


    return (tiimid)
















