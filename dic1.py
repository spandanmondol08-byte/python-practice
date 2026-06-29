n=int(input('Enter the no. of teams: '))
d={}
for i in range(n):
    names=input('Enter the names of the team : ')
    win=int(input('Enter the no. of wins: '))
    loss=int(input('Enter the no. of losses: '))
    d[names]=[win,loss]
print('The list of teams - ',d)
for ch in d:
    wp=(d[ch][0]/(d[ch][0]+d[ch][1]))*100
    print('Win percent of',ch,'is',wp)
l=[]
for ch in d:
    w=d[ch][0]
    wl=[ch,w]
    l.append(wl)
print('List of wins of teams: ',l)
lst=[]
for ch in d:
    w=d[ch][1]
    if w==0:
        lst.append(ch)
print('List of teams with only wins and no loss: ',lst)
