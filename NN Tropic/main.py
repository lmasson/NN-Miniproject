import q13

hn=q13.hopfield_network(200)
lim = 60
lim2 = 500
reterror = zeros(lim2+2)
x = zeros(lim)
mean = zeros(lim)
stdev = zeros(lim)
figure()
axis([0,lim+1,-15,50])
for j in range(lim-1):
    for i in range(lim2):
        hn.make_pattern(j+1)
        reterror[i+1]=hn.run(0,0.1)
        mean[j+1] = mean[j+1] + reterror[i+1]
    mean[j+1] = mean[j+1]/lim2
    x[j+1]=j+1
    for i in range(lim2):
        stdev[j+1]=stdev[j+1]+(reterror[i+1]-mean[j+1])*(reterror[i+1]-mean[j+1])
    stdev[j+1]=sqrt(stdev[j+1]/lim2)
    plot([j,j],[mean[j]-stdev[j],mean[j]+stdev[j]],'k')
    plot([j-0.5,j+0.5],[mean[j]+stdev[j],mean[j]+stdev[j]],'k')
    plot([j-0.5,j+0.5],[mean[j]-stdev[j],mean[j]-stdev[j]],'k')
plot([j+1,j+1],[mean[j+1]-stdev[j+1],mean[j+1]+stdev[j+1]],'k')
plot([j+0.5,j+1.5],[mean[j+1]+stdev[j+1],mean[j+1]+stdev[j+1]],'k')
plot([j+0.5,j+1.5],[mean[j+1]-stdev[j+1],mean[j+1]-stdev[j+1]],'k')
   
p1, = plot(x,mean,'g', lw=2)       
p2, =plot([0,lim],[2,2],'r')       
        
legend([p1,p2],["Mean retrival error", "2% error"]) 

xlabel('Number of patterns')
ylabel('Retrieval error')
#mean = mean/10
#print 'moyenne %.3f'%(mean)

