import matplotlib.pyplot as pl
trans=['Car','Public transit','Walking','Bicycle']
number=['40','30','20','10']
pl.title('The graph')
pl.pie(number,labels=trans,autopct='%1.0f%%')
pl.show()
