isldata=[
    {"team":"mumbai","mp":20,"won":12,"drawn":4,"los":4,"pts":40},
    {"team":"atk","mp":20,"won":12,"drawn":4,"los":4,"pts":40},
    {"team":"ne","mp":20,"won":8,"drawn":9,"los":3,"pts":33},
    {"team":"fcg","mp":20,"won":7,"drawn":10,"los":3,"pts":31},
    {"team":"hybd","mp":20,"won":6,"drawn":11,"los":3,"pts":29}
]
#highest points
points=max(list(map(lambda data:data["pts"],isldata)))
#print(points)
#hpt=list(filter(lambda team:team["pts"]==points,isldata))
#print(hpt)
#hptname=list(map(lambda team:team["team"],hpt))
#print(hptname)
rangeteam=list(filter(lambda data:(data["pts"]<=40) &(data["pts"]>30),isldata))
print(rangeteam)
