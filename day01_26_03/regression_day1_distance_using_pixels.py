# Predict Distance Using Pixels

"""
Your robot sees an object (like a bottle or face).

As the object moves:

It appears bigger in pixels when closer
Smaller when farther

You need to predict distance from camera using pixel size
"""

 #  Get Manual Dataset Input
def get_dataset_input():
    x = []
    y = []
    print("\n--== Dataset Values Input ==--\n")
    print ("--- Enter Values of Object Size in Pixels (X) ---\n")
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break
        try :
            user_input = float(user_input)
            x.append(user_input)
        except ValueError:
            print("Value can only be number only")

    print ("\n--- Enter Values of Distance in cm (Y) ---\n")
    while len(y) != len(x):
        user_input = input("Enter a number (or press Enter to finish): ")
        try :
            user_input = float(user_input)
            y.append(user_input)
        except ValueError:
            print("Value can only be number only")
    return list(x),list(y)

def calculate_regression_values(x,y):
    sum_xy = 0.0
    sum_x2 = 0.0
    n = len(x)
    # calculation of x2 & sumxy for slope
    for a,b in zip(x,y):
        sum_x2 += (a*a)
        sum_xy += (a*b)
    # calculation of means
    x_mean = sum(x) / n
    y_mean = sum(y)/ n

    #  calculate slope
    slope = ((sum_xy) -( n * x_mean * y_mean )) / ( sum_x2 - (n * x_mean * x_mean)) 
    # calculate intercept
    intercept = y_mean - (slope * x_mean)
    return slope , intercept

 #  Predict Distance Value Based on User Input

def calculate_predicted_value(x,slope,intercept):
     predicted_value = (slope*x) + intercept
     return predicted_value

def predict_value(slope,intercept):
 while True:
    user_value = input("\nEnter a 'Pixels' Value For Distance Prediction (or press Enter to finish): ")
    if user_value == "":
            break
    try :
            user_value = float(user_value)
            predicted_value = calculate_predicted_value(user_value,slope,intercept)
            print(f"\nPredicted Value for given value {user_value} is {predicted_value}")
    except ValueError:
            print("Value can only be number only")

   

def main():
    Pixels = []
    Distance = []
    Pixels,Distance = get_dataset_input()
    m,c = calculate_regression_values(Pixels,Distance)
    predict_value(m,c)

if __name__ == "__main__":
    main()
        


