# from function import get_student_data
# result = get_student_data("tony", 23, 'computer science')
# print(result)


# from temperature import celsius_to_fahrenheit,fahrenheit_to_celsius
# print("1.celsius to fahrenheit")
# print('2.fahrenheit to celsius')
# choice = input('choose conversion (1 or 2): ')

# if choice =='1':
#     c = float(input('enter temperature in celsius: '))
#     f = celsius_to_fahrenheit(c)
#     print(f'{c}⁰c = {f:.2f}⁰f')
# elif choice == "2":
#     f = float(inputt("enter temperature is celsius: "))
#     c = fahrenheit_to_celsius(f)
#     print(f'{f}⁰f = {c:.2f} ⁰c')
# else:
#     print("invalid choice")




from grading import student_result
num = int(input("how many students? "))
for i in range(num):
    print(f"instudent {i+1}:")
    name = input('enter name: ')
    score = int(input("enter score: "))
    result = student_result(name, score)
    print(f'-> {result{'name']} score{result{'csore'}} and got grade{result{'grade'}}')
                 
