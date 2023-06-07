sample_A=c(1,4,4,4,5,5,5,8)
sample_B=c(1,2,3,4,5,6,7,8)

n=length(sample_A)-1
donfidence=95
sd(sample_B)
mean(sample_B)
alpha=1-confidence/100

mean(sample_A)-alpha/2*sd(sample_A)/n**1/2

boxplot(sample_A,sample_B,col=c(5,6),horizontal = FALSE,names=c("Sample A","Sample B"))
hist(sample_A)
par(mfrow=c(2,2))
    
