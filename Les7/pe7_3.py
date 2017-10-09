scores = {
    'Anna':9.0,
    'Yu':9.5,
    'Hans':9.3,
    'Nicky':8.5,
    'Marco':8.0,
    'Ton':7.5,
    'Amy':7.0,
    'Ronald':6.5}

for i in scores:
    if float(scores[i]) > 9.0:
        print(i, scores[i])