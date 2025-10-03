# Go to the bottom of the code
# check 'example' variable to change input at line 57
# example is 2d array, each row is e1 e2 ..... en
# last column is the class and every other column is a feature

# learning rate can be changed inside the class, change self.learningRate at line 11

class PTA:
    def __init__(self):
        self.weights = {}   # stores my weights
        self.learningRate = 0.4 # change this for different learning rate, default should be 0.4

    def train(self, input):
        # initialize my weights and start them at zero for the bias and the features
        for i in range(len(input[0])):
            self.weights["w"+str(i)] = 0


        # loop through list of inputs and update weights
        r = 0
        while r < len(input):
            # initialize with bias calculated first
            predicted = 1 * self.weights["w0"]

            # adds up all the products to get v
            for i in range(len(input[r])-1):
                predicted += self.weights["w" + str(i+1)] * input[r][i]

            # u(v) to get the predicted value
            if predicted >= 0:
                predicted = 1
            else:
                predicted = 0

            print("Predicted: " + str(predicted) + "     " + "Actual: " + str(input[r][-1]))
            # check if predicted is the same as actual
            if predicted != input[r][-1]: # updates weights if predicted is wrong
                print("Prediction Wrong - Updating Weights...")
                # update the weight for the bias first
                self.weights["w0"] = self.weights["w0"] + (self.learningRate * (input[r][-1] - predicted) * 1)

                # update weights for the features
                for i in range(len(input[r])-1):
                    self.weights["w"+str(i+1)] = self.weights["w"+str(i+1)] + (self.learningRate * (input[r][-1] - predicted) * input[r][i])
                print("Updated Weights: ")
                print(self.weights)
                r = 0 # set r back to 0 to recheck all the inputs to see if all is predicted correctly
            else:
                r += 1 # if predicted is correct then move to the next input to check
        # print out of the final calculated weights
        print("Final Weights: ")
        print(self.weights)



# change this to test other stuff
example = [[1,0,0],
           [1,1,1],
           [0,0,0]]


# example = [[1,0,0,1,0],
#            [1,1,0,0,1],
#            [0,0,1,1,0]]

PTA().train(example)