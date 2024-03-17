a="Hello"
print(a)
# Menu options
options = ["Option 1", "Option 2", "Option 3", "Option 4"]
selected = [False] * len(options)  # Selection state of options

# Function to display the menu
def display_menu():
    for i, option in enumerate(options):
        prefix = "[x]" if selected[i] else "[ ]"
        print(f"{prefix} {option}")

# Function to handle the menu selection
def select_option(index):
    selected[index] = not selected[index]  # Toggle selection
    print(int(choice) - 11)
# Initial display
display_menu()

# Main loop
while True:
    print("\nUse the numbers to navigate the menu. Press 'Enter' to select, 'q' to quit.")
    choice = input("Enter your choice: ")

    if choice.lower() == 'q':
        break
    elif choice.isdigit() and int(choice) in range(1, len(options) + 1):
        select_option(int(choice) - 1)
        
        display_menu()
    else:
        print("Invalid selection. Please try again.")