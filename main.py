import torch
from gpt4all import GPT4All

# Check if GPU is available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

refiner_model = GPT4All(model_name="mistral-7b-openorca.gguf2.Q4_0.gguf", device="gpu") # Using GPU
#refiner_model = GPT4All(model_name="mistral-7b-openorca.gguf2.Q4_0.gguf", device="cpu") # Using CPU

def main():
    with refiner_model.chat_session():
        while True:
            user_input = input("You: ")
            if user_input.lower() == "quit":
                break
            print("processing answer")
            user_input = f"You: {user_input}"
            refined_response = refiner_model.generate(prompt=user_input)
            print(f"Bot: {refined_response}")

# Example usage
if __name__ == "__main__":
    main()
