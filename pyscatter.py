import matplotlib.pyplot as pl
trans=['Car','Public transit','Walking','Bicycle']
number=['40','30','20','10']
pl.title('The graph')
pl.xlabel('Transport type')
pl.ylabel('Numbers')
pl.hist(number)
pl.show()
