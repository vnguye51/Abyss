def AABB(a,b):
    if(a.x < b.x + b.width and
        a.x + a.width > b.x and 
        a.y < b.y + b.height and
        a.y + a.height > b.y):
        return True
    else:
        return False

def collision_resolution(collisions):
    for a,b in collisions:
        #resolve horizontal collision
        if a.xvel != 0 or b.xvel != 0:
            if abs(a.xvel) == abs(b.xvel):
                #!!!!!!!possible optimization only need to calculate horizontal/vertical collisions not both at once
                while AABB(a,b):
                    if a.x <= b.x:
                        a.x -= 1
                        b.x += 1
                    else:
                        a.x += 1
                        b.x -= 1
            elif abs(a.xvel) >= abs(b.xvel):
                while AABB(a,b):
                    if a.x <= b.x:
                        b.x += 1
                    else:
                        b.x -= 1
            else:
                while AABB(a,b):
                    if b.x <= a.x:
                        a.x += 1
                    else:
                        a.x -= 1
        #resolve vertical collision
        if a.yvel != 0 or b.yvel != 0:
            if a.yvel == b.yvel and a.yvel != 0:
                #!!!!!!!possible optimization only need to calculate horizontal/vertical collisions not both at once
                while AABB(a,b):
                    if a.y <= b.y:
                        a.y -= 1
                        b.y += 1
                    else:
                        a.y += 1
                        b.y -= 1
            elif abs(a.yvel) >= abs(b.yvel):
                while AABB(a,b):
                    if a.y <= b.y:
                        b.y += 1
                    else:
                        b.y -= 1
            else:
                while AABB(a,b):
                    if b.y <= a.y:
                        a.y += 1
                    else:
                        a.y -= 1