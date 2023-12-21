input_filepath = "C:/Users/krist/myCloud/Documents/__repositories/python/UdemyPythonIntro-master/Chapter4_Intermediate/test.txt"
output_filepath = "C:/Users/krist/myCloud/Documents/__repositories/python/UdemyPythonIntro-master/Chapter4_Intermediate/test_out.txt"


with open(input_filepath, "r") as file:
    content = file.readlines()


print(content)
content.append("Tom Tomerson\n")


with open(output_filepath, "w") as file:
    file.writelines(content)
