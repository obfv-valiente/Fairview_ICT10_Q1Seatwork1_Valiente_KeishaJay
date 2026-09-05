from pyscript import document, display

studentname = "Keisha Jay R. Valiente"
document.getElementById("name").innerHTML= f"Name: {studentname}"

age= 14
document.getElementById("age").innerHTML= f"Hypothetical age: {age}"

h3ight = 5.5
document.getElementById("h3ight").innerHTML= f"Height: {h3ight}"

countri3_s = ["Japan","Italy", "Malaysia"]
document.getElementById("countri3_s").innerHTML= f"Countries the robot wants 2visit: {', '.join(countri3_s)}"

student_type = True
document.getElementById("student_type").innerHTML= f"Status: {student_type}"

info = {
    "color":"Black",
    "car_brand" : "Mini Red SUV (U.S.A)",
    "shoe_size" : "9-10",
    "best_friend" : "Itself & other unauthorized anomalies"
}

document.getElementById("color").innerHTML= f"Wig Color: {info['color']}"
document.getElementById("car_brand").innerHTML= f"Fake Robot Car: {info['car_brand']}"
document.getElementById("shoe_size").innerHTML= f"Shoe Size: {info['shoe_size']}"
document.getElementById("best_friend").innerHTML= f"Bestfriend: {info['best_friend']}"


fruitsyum = ["Mango","Apple", "Watermelon"]
document.getElementById("fruitsyum").innerHTML= f"Prefered fruits: {', '.join(fruitsyum)}"


work = ("Monday","Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday")
document.getElementById("work").innerHTML= f"Work Schedule: {', '.join(work)}"


def add_num(e):
    document.getElementById("output1").innerHTML="" #clears previous result
    num1 = float(document.getElementById("input1").value) #get input value 
    num2 = float(document.getElementById("input2").value) #get input value

    result = num1 + num2

    display(f"Addition: {result}", target="output1")


def subtract_num(e):
    document.getElementById("output2").innerHTML="" #clears previous result
    num1 = float(document.getElementById("input1").value) #get input value 
    num2 = float(document.getElementById("input2").value) #get input value

    result = num1 - num2

    display(f"Subtraction: {result}", target="output2")


def multiply_num(e):
    document.getElementById("output3").innerHTML="" #clears previous result
    num1 = float(document.getElementById("input1").value) #get input value 
    num2 = float(document.getElementById("input2").value) #get input value

    result = num1 - num2

    display(f"Multiplication: {result}", target="output3")


def divide_num(e):
    document.getElementById("output4").innerHTML="" #clears previous result
    num1 = float(document.getElementById("input1").value) #get input value 
    num2 = float(document.getElementById("input2").value) #get input value

    result = num1 - num2

    display(f"Divide: {result}", target="output4")
