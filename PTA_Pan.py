class PTA:
    def __init__(self):
        self.weights = {}
        self.learningRate = 0.4

    def train(self, input):
        # initialize my weights and start them at zero for the bias and the features
        for i in range(len(input[0])):
            self.weights["w"+str(i)] = 0


        # loop through list of inputs and update weights
        r = 0
        while r < len(input):
            # initialize with bias calculated first
            predicted = 1 * self.weights["w0"]

            #
            for i in range(len(input[r])-1):
                predicted += self.weights["w" + str(i+1)] * input[r][i]

            # u(v) to get the predicted value
            if predicted >= 0:
                predicted = 1
            else:
                predicted = 0

            print("Predicted: " + str(predicted) + "     " + "Actual: " + str(input[r][-1]))

            if predicted != input[r][-1]: # updates weights if predicted is wrong
                print("Prediction Wrong - Updating Weights")
                # update the weight for the bias first
                self.weights["w0"] = self.weights["w0"] + (self.learningRate * (input[r][-1] - predicted) * 1)

                # update weights for the features
                for i in range(len(input[r])-1):
                    self.weights["w"+str(i+1)] = self.weights["w"+str(i+1)] + (self.learningRate * (input[r][-1] - predicted) * input[r][i])

                r = 0 # set r back to 0 to recheck all the inputs to see if all is predicted correctly
                continue
            else:
                r+=1 # if predicted is correct then move to the next input to check

        print(self.weights)




example = [[1,0,0],
           [1,1,1],
           [0,0,0]]

# example = [[0,0,1],
#            [0,1,0],
#            [1,0,0],
#            [1,1,0],]

PTA().train(example)