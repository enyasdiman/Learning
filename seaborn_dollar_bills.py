# Import seaborn
import seaborn as sns

# Use pairplot and set the hue to be our class
sns.pairplot(banknotes, hue = "class") 

# Show the plot
plt.show()

# Describe the data
print('Dataset stats: \n', banknotes.describe())

# Count the number of observations of each class
print('Observations per class: \n', banknotes["class"].value_counts())
