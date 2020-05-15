# Compile your model
model.compile(optimizer= "adam", loss = "mse")

print("Training started..., this can take a while:")

# Fit your model on your data for 30 epochs
model.fit(time_steps, y_positions, epochs = 30)

# Evaluate your model 
print("Final lost value:",model.evaluate(time_steps, y_positions))
