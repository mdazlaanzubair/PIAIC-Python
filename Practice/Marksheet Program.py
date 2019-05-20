# dictionary of subjects
marks_of_subjects = {}

# instructions to the user regarding this program
list_of_subjects = ["Mathematics", "Physics", "Chemistry", "Urdu", "English", "Pak-Studies", "Computer-Science", "Biology", "Islamic-Studies", "Sindhi"]
example = "'Mathematics, 96' or 'english, 75'"
separator = ", "
instruction_1 = """
Kindle enter your 'marks' with their respective 'subjects' separated by 'commas' like this:
{}\n
*** NOTE: Make sure your subjects must be in the list otherwise you'll get wrong results. ***\n
List of Subjects: {} 
"""
print(instruction_1.format(example, separator.join(list_of_subjects)))

# getting number of subject a user want to generate a mark-sheet
no_of_subjects = int(input("Number of subjects: "))

# iterating to get mentioned number of inputs in above step
for i in range(0, no_of_subjects):
    a, b = input("Enter your 'marks' with their respective 'subjects' separated by 'commas': ").split(",")
    marks_of_subjects[a] = float(b)  # adding the element

# performing mark-sheet calculations
total_marks = 0
for i in marks_of_subjects.values():
    total_marks = total_marks + i

subjects_count = len(marks_of_subjects)
percentage = (total_marks*100)/(subjects_count*100)
average = total_marks/subjects_count
gpa = percentage/25

print("\n Marks Obtained:")
print("==================")

for key, value in marks_of_subjects.items():
    key = key.title()
    print(key, ":", value)

print("\n Result:")
print("==================")
print("Total Marks Obtained:", total_marks)
print("Percentage Obtained:", percentage)
print("Average:", average)
print("Standardize GPA:", gpa)