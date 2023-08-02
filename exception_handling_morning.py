# Create an empty dictionary to store student responses
my_dict = {}

# Function to prompt students and collect their responses
def prompt_students():
    while True:
        student_name = input("Enter student name (or 'r' to quit): ")
        if student_name == 'r':
            break
        mental_health_status = input("How is your mental health? ")
        my_dict[student_name] = mental_health_status

# Function to display the collected responses
def display_responses():
    print("\nMental health responses:")
    for student, status in my_dict.items():
        print(f"{student}: {status}")

# Prompt students for their responses
prompt_students()

# Display the collected responses
display_responses()
