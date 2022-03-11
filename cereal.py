import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
pd.options.display.max_rows = 9999
pd.options.display.max_columns = 9999
df = pd.read_csv('cereal.csv')
df = dict(zip(df.name, df.sugars))
df = fat
finished = False
while finished == False: #while finished = false, the while loop will continue to run
    cereal1 = input("Enter a cereal: ")
    cereal2 = input("Enter a cereal: ")
    cereal1_sugar = df.get(cereal1)
    cereal2_sugar = df.get(cereal2)
    cereal1_fats = df.get(cereal1)
    cereal2_fats = df.get(cereal2)

    print(f"{cereal1} has {cereal1_sugar} grams of sugar and {cereal1_fats} grams of fat {cereal2} has {cereal2_sugar} grams of sugar and {cereal2_fats} grams of fat")
    if cereal1_sugar > cereal2_sugar:
        print(f"{cereal2} has less sugar than {cereal1}")
    if cereal1_sugar < cereal2_sugar:
        print(f"{cereal2} has more sugar than {cereal1}")
    if cereal1_sugar == cereal2_sugar:
        print(f"{cereal2} has same amount as {cereal1}")
    x = np.array([cereal1, cereal2])
    y = np.array([cereal1_sugar, cereal2_sugar, cereal1_fats, cereal2_fats])

    plt.bar(x,y)
    plt.show()
    choice = input("Do you want to make another choose? ")
    if choice.lower != "yes":   
        finish = True 
