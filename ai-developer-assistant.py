from gpt4all import GPT4All

# Path to your local model
MODEL_PATH = "YOUR_MODEL_PATH_HERE"
model = GPT4All(MODEL_PATH)

def ask_ai(prompt: str) -> str:
    try:
        # Standard generation settings
        response = model.generate(prompt)
        return response
    except Exception as e:
        return f"[AI Error] {e}"

def main():
    print("=== Free AI Developer Assistant ===")
    
    # Get user input
    idea = input("Enter your feature idea: ")
    
    # Step 1: Task Breakdown
    tasks = ask_ai(f"Break down this feature into actionable steps: {idea}")
    print("\n--- Task Breakdown ---")
    print(tasks)
    
    # Step 2: Technical Specification
    spec = ask_ai(f"Write a technical specification based on these tasks: {tasks}")
    print("\n--- Technical Spec ---")
    print(spec)
    
    # Step 3: Code Generation
    code = ask_ai(f"Provide Python starter code based on this spec: {spec}")
    print("\n--- Starter Code ---")
    print(code)
    
    # Step 4: Edge Case Analysis
    edge = ask_ai(f"List potential edge cases for this implementation: {spec}")
    print("\n--- Edge Cases ---")
    print(edge)

if __name__ == "__main__":
    main()
    