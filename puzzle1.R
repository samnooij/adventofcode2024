#!/usr/bin/env Rscript

library(here)

input_data <- read.delim(here("Documents/adventofcode2024/input/puzzle1.txt"),
                         sep = " ", header = F, strip.white = T)

## Part 1:
## Find the total distance between the two columns.

sorted_col1 <- sort(input_data[,1])
sorted_col2 <- sort(input_data[,ncol(input_data)])

total_distance <- sum(abs(sorted_col1 - sorted_col2))

print(total_distance)

## Part 2:
## Calculate the similarity score between the columns.
occurrences <- c()
for (number in sorted_col1) {
  occurrences <- c(occurrences, sum(sorted_col2 == number))
}

# The similarity score is the sum of each number multiplied by
# the number of occurrences in the second column:
similarity_score <- sum(sorted_col1 * occurrences)

print(similarity_score)
