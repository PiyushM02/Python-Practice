def course_generator():
    yield ("Computer Science", 5)
    # Write your code below:
    yield ("Art", 10)
    yield ("Business", 15)

def add_five_students(courses):
  for course, num_students in courses:
    yield (course, num_students + 5)


increased_courses = add_five_students(course_generator())
for course in increased_courses:
  print(course)
    
