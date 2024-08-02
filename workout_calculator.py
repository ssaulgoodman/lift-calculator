def custom_round(number):
    decimal_part = number % 1
    if decimal_part < 0.5:
        return int(number)
    else:
        return int(number) + 1

def calculate_sets(one_rep_max):
    training_set = custom_round(0.90 * one_rep_max)
    
    sets = [
        (5, custom_round(0.65 * training_set)),
        (5, custom_round(0.75 * training_set)),
        (10, custom_round(0.85 * training_set)),
        (5, custom_round(0.75 * training_set)),
        (15, custom_round(0.65 * training_set))
    ]
    
    print(f"Your training set (90% of 1RM): {training_set}")
    print("\nCalculated sets:")
    for i, (reps, weight) in enumerate(sets, 1):
        print(f"Set {i}: {reps} reps at {weight}")

def main():
    try:
        one_rep_max = float(input("Enter your 1 rep max: "))
        calculate_sets(one_rep_max)
    except ValueError:
        print("Please enter a valid number for your 1 rep max.")

if __name__ == "__main__":
    main()