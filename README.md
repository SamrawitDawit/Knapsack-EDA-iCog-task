# Univariate and Multivariate Evolutionary Distribution Algorithms (EDAs)

Evolutionary Distribution Algorithms (EDAs) are optimization tools used to solve problems by finding the best solutions. Instead of traditional methods like crossover and mutation in genetic algorithms, EDAs use probability models to guide their search for better answers. These algorithms are divided into **Univariate EDAs** and **Multivariate EDAs**, depending on how they handle relationships between variables.

---

## Univariate EDAs

Univariate EDAs assume that all variables in a problem are independent of each other. This means they treat each variable as separate and do not consider how one might affect another.

### Steps in Univariate EDAs:
1. **Select Solutions**: Pick the best solutions from the current group (population) based on their performance.
2. **Build a Model**: Create a simple probability model for each variable independently.
3. **Generate New Solutions**: Use the model to create new possible solutions.
4. **Update Population**: Replace the old solutions with the new ones.

### Types of Univariate EDAs:
- **Compact Genetic Algorithm (cGA)**: Uses a simple probability vector to decide values for each variable.
- **Population-Based Incremental Learning (PBIL)**: Updates a probability vector using the best solutions found so far.
- **Univariate Marginal Distribution Algorithm (UMDA)**: Models each variable separately using basic statistics.

---

## Multivariate EDAs

Multivariate EDAs, unlike univariate ones, look at how variables interact or depend on each other. These algorithms use advanced probability models to capture relationships between variables, making them useful for more complex problems.

### Steps in Multivariate EDAs:
1. **Select Solutions**: Choose the best solutions based on performance.
2. **Build a Complex Model**: Create a model that shows how variables are connected.
3. **Generate New Solutions**: Sample new solutions based on this model.
4. **Update Population**: Replace old solutions with the new ones.

### Types of Multivariate EDAs:
- **Bayesian Optimization Algorithm (BOA)**: Uses a graph-based model to represent variable dependencies.
- **Estimation of Multivariate Normal Algorithm (EMNA)**: Assumes variables follow a Gaussian distribution and captures their relationships using a covariance matrix.
- **Factorized Distribution Algorithm (FDA)**: Breaks down the joint distribution into smaller parts based on the problem's structure.

---

## Key Differences Between Univariate and Multivariate EDAs

| **Aspect**         | **Univariate EDAs**                      | **Multivariate EDAs**                             |
|---------------------|------------------------------------------|--------------------------------------------------|
| **Variable Relationships** | Assumes variables are independent.        | Considers relationships between variables.       |
| **Model Type**      | Simple, focusing on individual variables. | Complex, showing how variables are connected.    |
| **Complexity**      | Easier to use and faster.                | More advanced and slower.                        |
| **Best For**        | Problems where variables don't interact much. | Problems where variables are strongly linked.    |
| **Examples**        | cGA, PBIL, UMDA                         | BOA, EMNA, FDA                                   |

---

## Applications of EDAs in Real-World Problems

1. **Engineering Design**  
   EDAs help optimize designs, like creating efficient airplane wings. Multivariate EDAs can consider how wing length, shape, and material work together to improve performance.

2. **Biology and Medicine**  
   In bioinformatics, EDAs are used for tasks like predicting protein structures or understanding gene networks. Multivariate EDAs are great at finding patterns in complex data.

3. **Financial Planning**  
   EDAs can optimize investment portfolios by modeling how different assets (like stocks) are related to balance risk and return.

4. **Scheduling Jobs**  
   Univariate EDAs work for simple task scheduling, but multivariate EDAs handle more complex schedules with many dependencies, like in factories or logistics.

5. **Healthcare**  
   In personalized medicine, EDAs can analyze patient data to find the best treatment plans by understanding relationships between symptoms and treatments.

### Example: Logistics Optimization
In delivery planning, multivariate EDAs can model how routes, traffic, and delivery times interact. This helps create efficient schedules that save time and fuel.

---

## Conclusion

Univariate and Multivariate EDAs solve different kinds of problems:  
- **Univariate EDAs** are simpler and faster but ignore variable relationships.  
- **Multivariate EDAs** are better for complex problems with strong interactions.  

Both have wide applications, from engineering to healthcare, making them powerful tools for real-world problem-solving.
