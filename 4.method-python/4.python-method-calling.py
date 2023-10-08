def my_name_is():
    print("My name is Sabbir hasan")


def i_have_enrolled_course(course_name):
    print(f"I have enrolled in a course named {course_name}")


def i_have_learning(backend, frontend):
    return f"Learning {backend}, {frontend}"


course_and_learn = [
         
   {
       "course":"Python and web",
       "backend":"Java",
       "frontend": "Python, HTML, CSS"
   },
   {
       "course":"Java Spring Boot",
       "backend":"Java",
       "frontend": "Hibernet, HTML, CSS"
   },
   {
       "course": "C# & ASP.NET Core",
       "backend": "C#",
       "frontend": "Razor, Entity Framework"
   },
    { "course":"MERN Development",
      "backend":"Node",
      "frontend": "React, HTML, CSS"
      },
    { "course":"PHP & Laravel",
      "backend":"PHP",
      "frontend":"Blade, Eloquent"}
]


for item in course_and_learn:
    course_name=item["course"]
    backend=item["backend"]
    frontend=item["frontend"]



    my_name_is()
    i_have_enrolled_course(course_name)
    result = i_have_learning(backend, frontend)
    print(result)




