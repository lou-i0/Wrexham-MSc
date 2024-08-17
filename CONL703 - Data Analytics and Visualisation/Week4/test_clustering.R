# library(tidyr)
# library(dplyr)
# library(ggplot2)
# library(cluster)
# library(lattice)
# library(graphics)
# library(grid)
# library(gridExtra)
# 
# 
# # Import in relevant data to use 
# tit_input <- read.csv('D:\\Coding\\DataSets\\Titanic_passengers.csv')
# 
# # Remove passenger ID, as not useable for kmeans clustering
# ktit_data <- tit_input %>% select(-PassengerId, -Name, -Ticket, -Cabin, -Embarked, -Age) %>% mutate(male = if_else(Sex == 'male',1,0)) %>% select(-Sex)
# 
# # Producing an elbow chart, to work out the number of clusters best suited for the data.
# wss <- numeric(15)
# 
# for(k in 1:15) wss[k] <- sum(kmeans(ktit_data , centers = k, nstart = 25)$withines)
# 
# plot(x = 1:15,y =  wss, type = 'b', xlab = 'Number of clusters', ylab = 'within sum of squares')
# 
# km <- kmeans(x = ktit_data,centers = 3, nstart = 25)
# km



# Installing Packages
install.packages("ClusterR")
install.packages("cluster")

# Loading package
library(ClusterR)
library(cluster)

# Removing initial label of 
# Species from original dataset
iris_1 <- iris[, -5]

# Fitting K-Means clustering Model 
# to training dataset
set.seed(240) # Setting seed
kmeans.re <- kmeans(iris_1, centers = 3, nstart = 20)
kmeans.re

# Cluster identification for 
# each observation
kmeans.re$cluster

# Confusion Matrix
cm <- table(iris$Species, kmeans.re$cluster)
cm

# Model Evaluation and visualization
plot(iris_1[c("Sepal.Length", "Sepal.Width")])
plot(iris_1[c("Sepal.Length", "Sepal.Width")], 
     col = kmeans.re$cluster)
plot(iris_1[c("Sepal.Length", "Sepal.Width")], 
     col = kmeans.re$cluster, 
     main = "K-means with 3 clusters")

## Plotiing cluster centers
kmeans.re$centers
kmeans.re$centers[, c("Sepal.Length", "Sepal.Width")]

# cex is font size, pch is symbol
points(kmeans.re$centers[, c("Sepal.Length", "Sepal.Width")], 
       col = 1:3, pch = 8, cex = 3) 

## Visualizing clusters
y_kmeans <- kmeans.re$cluster
clusplot(iris_1[, c("Sepal.Length", "Sepal.Width")],
         y_kmeans,
         lines = 0,
         shade = TRUE,
         color = TRUE,
         labels = 2,
         plotchar = FALSE,
         span = TRUE,
         main = paste("Cluster iris"),
         xlab = 'Sepal.Length',
         ylab = 'Sepal.Width')
