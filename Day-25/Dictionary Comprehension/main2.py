sentence  = "What is the Airspeed Velocity of an unladen swallow?"

result= { word:len(word) for word in sentence.split() }

print(result)