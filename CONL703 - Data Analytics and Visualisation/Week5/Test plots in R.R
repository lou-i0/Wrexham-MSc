data(mtcars)

dotchart(
          x = mtcars$mpg
          ,labels = row.names(mtcars)
          ,cex=.7
          ,main='Mile Per gallon (MPG) of car models'
          ,xlab="MPG"
        )

barplot(
        table(mtcars$cyl)
        ,main = "distrbution of cyclinders in car types"
        ,xlab= 'Number of Cylinders'
        )

hist(x = mtcars$hp)

d <- density(mtcars$wt)
plot(d)


library(ggplot2)
library(lattice)
data("diamonds")


niceDiamonds <- diamonds[diamonds$cut =='Premium'| diamonds$cut =='Ideal',]

summary(diamonds$cut)
  summary(niceDiamonds$cut)

  # plot density plot  of diamoND PICES
  ggplot(niceDiamonds, aes(x = price, fill = cut)
        ) + geom_density(alpha=.3, color=NA)
  
  # plot density plot  of diamoND PICES using log10 scale
  ggplot(niceDiamonds, aes(x = log10(price), fill = cut)
  ) + geom_density(alpha=.3, color=NA)
  

#  plot a linear regression line  on sample data 
x<- runif(75,0,10)
x<- sort(x)

y <- 200 + x^3 - 10 * x^2 + x + rnorm(n=75, mean = 0, sd = 20)

lr <- lm(formula = y ~ x)

poly <- loess(y ~ x)

fit <- predict(poly)

plot(x,y)

#  draw fitted line for linear regression
points(x,lr$coefficients[1] + lr$coefficients[2] *x, type = "l", col = 2)

# draw loes line to fir on points
points(x, fit, type = "l", col=4)
       