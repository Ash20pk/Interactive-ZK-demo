import hashlib

def generate_proof(secret_word):
    # Generate a proof hash based on the secret word
    proof_hash = hashlib.sha256(secret_word.encode()).hexdigest()
    return proof_hash

def verify_proof(proof_hash, user_proof):
    # Compare the user's proof hash with the original proof hash
    if user_proof == proof_hash:
        return True
    else:
        return False

# Welcome message
print("Welcome to the Secret Word Zero-Knowledge Proof System!")
print("In this system, the prover will choose a secret word and generate a proof.")
print("The verifier will then verify the prover's knowledge without learning the secret word.")
print()

# Prover's perspective
print("Prover's Perspective:")
secret_word = input("Prover, enter your secret word: ")
proof_hash = generate_proof(secret_word)
print("Prover, your proof hash is:", proof_hash)
print()

# Verifier's perspective
print("Verifier's Perspective:")
print("The verifier receives the proof hash from the prover.")
print("Verifier, you received the following proof hash:", proof_hash)
print()

user_proof = input("Verifier, ask the prover to provide the proof hash: ")

if verify_proof(proof_hash, user_proof):
    print("\nVerifier: The provided proof hash matches the original proof hash.")
    print("Verifier: You can be confident that the prover knows the secret word without learning it.")
else:
    print("\nVerifier: The provided proof hash does not match the original proof hash.")
    print("Verifier: You cannot verify the prover's knowledge of the secret word.")

# Additional information
print("\nAdditional Information:")
print("In this demo, the verifier receives the proof hash from the prover.")
print("The verifier then asks the prover to provide the proof hash and verifies it against the original proof hash.")
print("If the hashes match, the verifier can be confident that the prover knows the secret word.")
print("However, the verifier does not learn the actual secret word during this process.")
print("This showcases the concept of zero-knowledge proofs, where knowledge can be verified without revealing the secret.")