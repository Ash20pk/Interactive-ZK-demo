import random

def generate_cave_paths():
    # Randomly generate the correct path (either "A" or "B")
    correct_path = random.choice(['A', 'B'])
    return correct_path

def prove_knowledge(correct_path, num_iterations):
    successful_iterations = 0
    
    for _ in range(num_iterations):
        # Ali Baba enters the cave through a random path
        chosen_path = random.choice(['A', 'B'])
        
        # Victor (the user) chooses the path for Ali Baba to return from
        print(f"\nIteration {_ + 1}:")
        print("Ali Baba (Prover) has entered the cave.")
        requested_path = input("Enter the path you want Ali Baba to return from (A/B): ").upper()
        
        if requested_path == chosen_path:
            # Ali Baba can return from the requested path
            successful_iterations += 1
            print("Ali Baba (Prover) successfully returned from the requested path.")
        else:
            # Ali Baba cannot return from the requested path
            print("Ali Baba (Prover) failed to return from the requested path.")
            return 0
        
        confidence = (1 - (1 / 2) ** (_ + 1)) * 100
        print(f"Victor's (Verifier) confidence: {confidence:.2f}%")
    
    return confidence

def main():
    print("Welcome to the Zero-Knowledge Proof Interactive Demo!")
    print("In this demo, you will play the role of Victor (the Verifier).")
    print("Ali Baba (the Prover) claims to know the secret word that opens the magic door in the cave.")
    
    # Generate the correct path in the cave
    correct_path = generate_cave_paths()
    
    print("\nYou and Ali Baba agree on naming the two paths in the cave as A and B.")
    
    # Prompt Victor (the user) to enter the number of iterations
    num_iterations = int(input("Enter the number of times you want Ali Baba to demonstrate his knowledge: "))
    
    # Simulate the Zero-Knowledge Proof iterations
    confidence = prove_knowledge(correct_path, num_iterations)
    
    if confidence > 0:
        print(f"\nAfter {num_iterations} iterations, your (Victor, the Verifier) confidence that Ali Baba knows the secret word is {confidence:.2f}%.")
        print("As the number of successful iterations increases, your confidence approaches, but never reaches, 100%.")
    else:
        print("\nAli Baba (Prover) failed to demonstrate knowledge of the secret word.")
        print("You (Victor, the Verifier) have caught Ali Baba lying and are now certain that he does not know the secret word.")
    
    print("\nSee, without revealing the secret word, you (Victor, the Verifier) could verify if Ali Baba (Prover) really knows the secret. This is how Zero-Knowledge Proofs work!")

if __name__ == '__main__':
    main()