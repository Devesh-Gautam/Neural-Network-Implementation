# inputs = [1.2, 2.3, 3.4, 4.5, 5.6]
# weights = [0.1, 0.2, 0.3, 0.4, 0.5]
# biases =  0.5

# output = sum(i * w for i, w in zip(inputs, weights)) + biases
# print(output)

# 4 inputs and 3 neurones
# inputs = [1, 2, 3, 2.5]
# weights = [
#     [0.2, 0.8, -0.5, 1.0],
#     [0.5, -0.91, 0.26, -0.5],
#     [-0.26, -0.27, 0.17, 0.87]]
# biases = [2, 3, 0.5]

# outputs = []
# for i in range(len(weights)):
#     output = sum(inputs[j] * weights[i][j] for j in range(len(inputs))) + biases[i]
#     outputs.append(output)
    
# print(outputs)  # Output: [6.5, 8.0, 9.5]