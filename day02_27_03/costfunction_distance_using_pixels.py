# Predict Distance Using Pixels

# Day 01 

"""
Your robot sees an object (like a bottle or face).

As the object moves:

It appears bigger in pixels when closer
Smaller when farther

You need to predict distance from camera using pixel size
"""
#  Day 02
"""
1. Use Your Existing System
Dataset input (X, Y)
Regression calculation (m, b)
2. Compute Model Error

For EACH data point:

Calculate predicted value
Compare with actual value
Compute error
3. Aggregate Error
Combine all individual errors into ONE number
This number = model cost
4. Output MUST include:
Model Summary
slope
intercept
total cost
Detailed Breakdown (VERY IMPORTANT)

For EACH point:

Input (X)
Actual value (Y)
Predicted value
Error
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

#  Calculate Regression Values - Slope & Intercept
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

#  x y contain list of dataset vlaues inputted manually
 # Calculation of cost value
def calculate_cost_function(x,y,slope,intercept):
     n = len(x)
     total_cost = 0
     for a,b in zip(x,y):
          cost = a -((slope*a)+ intercept )
          total_cost += (cost * cost)
     return total_cost/(2*n)

# All dataset points
def display_dataset(x,y,slope,intercept):
    error_values = []
    predicted_values = []
    for a,b in zip(x,y):
        index = x.index(a)
        actual_value = y[index]
        predicted_value = calculate_predicted_value(a,slope,intercept)
        error = actual_value - predicted_value
        error_values.append(error)
        predicted_values.append(predicted_value)
    print("\nDataset Breakdown")
    i = 0 
    while i < len(x) :
        print(f"\nInput X : {x[i]}     |     Actual Y : {y[i]}     |     Predicted Ŷ : {predicted_values[i]}     |     Error : {error_values[i]}")
        i += 1




 #  Prediciting Final Output Values For Model with Error - COst Function
def predict_value(x,y,slope,intercept,error):
 print(f"\nModel Trained \nSlope : {slope} \nIntercept : {intercept}\nError (Total Model Cost) : {error}")
 display_dataset(x,y,slope,intercept)

 while True:
    user_value = input("\nEnter a 'Pixels' Value For Distance Prediction (or press Enter to finish): ")
    if user_value == "":
            break
    try :
            user_value = float(user_value)
            predicted_value = calculate_predicted_value(user_value,slope,intercept)
            print("\nOutput Breakdown")
            if user_value not in x:
                 print(f"\nPredicted Value : {predicted_value}")
                 print("\nValue not in model dataset . Continue with Dataset Value to get cost error details.")
            else:
             display_dataset(x,y,slope,intercept)
             index = x.index(user_value)
             actual_value = y[index]
             error = actual_value - predicted_value
             
             print(f"\nActual Value : {actual_value} \nPredicted Value : {predicted_value} \nError : {error }")
            
    except ValueError:
            print("Value can only be number only")

   

def main():
    Pixels = []
    Distance = []
    Pixels,Distance = get_dataset_input()
    m,c = calculate_regression_values(Pixels,Distance)
    model_cost = calculate_cost_function(Pixels,Distance,m,c)
    predict_value(Pixels,Distance,m,c,model_cost)

if __name__ == "__main__":
 try:
    main()
 except EOFError , KeyboardInterrupt :
  print("\n\nSystem Interuption Detected. Exiting The Program ....")
        


