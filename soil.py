from pomegranate import *
import numpy

#Observation models

clean = DiscreteDistribution({
    "Safe Level":0.9,
    "Slight Elevated": 0.1,
    "Hazardous": 0.0,
})

moderate = DiscreteDistribution({
    "Safe Level":0.2,
    "Slight Elevated": 0.6,
    "Hazardous": 0.2,
})

high = DiscreteDistribution({
    "Safe Level":0.0,
    "Slight Elevated": 0.3,
    "Hazardous": 0.7,
})

states = [clean, moderate, high]

#Transition model
transitions = numpy.array([
    [0.8, 0.2, 0.0],  # Clean -> Clean/Moderate/High
    [0.1, 0.7, 0.2],  # Moderate -> Clean/Moderate/High
    [0.0, 0.3, 0.7]   # High -> Clean/Moderate/High
])

# Starting probabilities
starts = numpy.array([1/3, 1/3, 1/3]) #We don't know the initial state

# Create the model
model = HiddenMarkovModel.from_matrix(
    transitions, states, starts,
    state_names=["clear", "moderate", "high"]
)
model.bake()

# Observations from instrument
observations = ["Slight Elevated", "Hazardous", "Hazardous"]

# Run forward algorithm
fwd = model.forward(observations)   # only one return now

# Convert from log to normal probabilities
fwd = numpy.exp(fwd)

# Normalize at each step so rows sum to 1
fwd = fwd / fwd.sum(axis=1, keepdims=True)

# The last row = probabilities after 3 readings
final_probs = fwd[-1]

print("Final probability distribution after 3 readings:")
print("   Clear    =", final_probs[0])
print("   Moderate =", final_probs[1])
print("   High     =", final_probs[2])

print("\nTherefore, probability the site is HIGH = {:.2f}%".format(final_probs[2]*100))

# Q2. Most likely hidden path
# ===============================
logp, path = model.viterbi(observations)
most_likely_path = [state.name for i, state in path[1:]]  # skip root
print("Most likely hidden path =", " → ".join(most_likely_path))

# ===============================
# Q3. Interpretation in words
# ===============================
print("\nInterpretation:")
print(f"After 3 sensor readings, the model estimates there is a {final_probs[2]*100:.2f}% "
      f"chance the site is HIGHLY polluted.")
print(f"The most likely pollution evolution was: {' → '.join(most_likely_path)}.")