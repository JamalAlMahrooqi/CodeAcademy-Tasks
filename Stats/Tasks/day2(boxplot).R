set.seed(123)
var1=rnorm(100,24,2)
boxplot(var1,horizontal = TRUE ,col='red',outline = FALSE)
fivenum(var1)
summary(var1)
var1[2]
var1[3]=var1[3]+40
var1[5]=var1[5]+40
