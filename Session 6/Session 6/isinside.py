def is_inside(l1,l2):
    if l2[0]+l2[3] > l1[0] > l2[0] and l2[1]+l2[2]>l1[1]>l2[1]:
        return True
    else:
        return False
is_inside([200, 120], [140, 60, 100, 200])
is_inside([100, 120], [140, 60, 100, 200])
