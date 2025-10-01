class WINNOW:
    def __init__(self):
        self.weights = {}
        self.alpha = 2
        self.bias = None

    def train(self, input):
        # calculate theta
        self.bias = len(input[0]) - 1 - 0.1

        # initialize my weights for each feature to 1
        for i in range(len(input[0])-1):
            self.weights["w"+str(i+1)] = 1

        # loop through list of inputs and update weights
        r = 0
        while r < len(input):
            predicted = 0

            # adds up all the products
            for i in range(len(input[r])-1):
                predicted += self.weights["w" + str(i+1)] * input[r][i]

            # h(x) to get the predicted value
            if predicted > self.bias:
                predicted = 1
            else:
                predicted = 0

            print("Predicted: " + str(predicted) + "     " + "Actual: " + str(input[r][-1]))

            if predicted != input[r][-1]:
                print("Prediction Wrong - Updating Weights")

                # update weights for the features
                for i in range(len(input[r])-1):
                    if input[r][i] == 1:
                        self.weights["w"+str(i+1)] = self.weights["w"+str(i+1)] * (self.alpha ** (input[r][-1] - predicted))
                r = 0 # set r back to 0 to recheck all the inputs to see if all is predicted correctly
                continue
            else:
                r+=1 # if predicted is correct then move to the next input to check
        # print out of the final calculated weights
        print(self.weights)

example = [[1,0,0],
           [1,1,1],
           [0,0,0]]

# example = [[1,1,1,1],
#            [1,1,0,0],
#            [1,0,1,0],
#            [1,0,0,0],
#            [0,1,1,1],
#            [0,1,0,0],
#            [0,0,1,0],
#            [0,0,0,0],]

WINNOW().train(example)


