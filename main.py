from pyscript import document, display

studentname = "Keisha Jay R. Valiente" # string data type
document.getElementById("name").innerHTML= f"Name: {studentname}" #uses whatever value it currently holds

age= 14 #integer data type
document.getElementById("age").innerHTML= f"Hypothetical age: {age}"

h3ight = 5.5 #float data type
document.getElementById("h3ight").innerHTML= f"Height: {h3ight}"

countri3_s = ["Japan","Italy", "Malaysia"] #list data type
document.getElementById("countri3_s").innerHTML= f"Countries the robot wants 2visit: {', '.join(countri3_s)}" #holds 3 strings

student_type = True #Boolean data type
document.getElementById("student_type").innerHTML= f"Status: {student_type}"

info = {
    "color":"Black",
    "car_brand" : "Mini Red SUV (U.S.A)",
    "shoe_size" : "9-10",
    "best_friend" : "Itself & other unauthorized anomalies"
}#dictionary type / each key ties into a value or rather uses a pair / mutuble

document.getElementById("color").innerHTML= f"Wig Color: {info['color']}" # uses 'info' to look into the dictionary n grab the value
document.getElementById("car_brand").innerHTML= f"Fake Robot Car: {info['car_brand']}"
document.getElementById("shoe_size").innerHTML= f"Shoe Size: {info['shoe_size']}"
document.getElementById("best_friend").innerHTML= f"Bestfriend: {info['best_friend']}" 


fruitsyum = ["Mango","Apple", "Watermelon"] #list/type -- a collection of values
document.getElementById("fruitsyum").innerHTML= f"Prefered fruits: {', '.join(fruitsyum)}" #uses 'join' to join/stick things together or rather the values inside 'fruitsyum'


work = ("Monday","Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday") #tuple data type-- immutuble compared to list,set, and dictionary
document.getElementById("work").innerHTML= f"Work Schedule: {', '.join(work)}"


def add_num(e):
    document.getElementById("output1").innerHTML="" #clears previous result
    num1 = float(document.getElementById("input1").value) #get input value 
    num2 = float(document.getElementById("input2").value) #get input value

    result = num1 + num2 #use's the input value from the above to calculate

    display(f"Addition: {result}", target="output1")
#uses the "<div id="output1"></div> " to display itself.. hence 'target' likewise to the rest

def subtract_num(e):
    document.getElementById("output2").innerHTML="" #clears previous result
    num1 = float(document.getElementById("input1").value) #get input value 
    num2 = float(document.getElementById("input2").value) #get input value

    result = num1 - num2

    display(f"Subtraction: {result}", target="output2")
#uses the alt "<div id="output2"></div> " to display itself.. hence 'target' likewise to the rest

def multiply_num(e):
    document.getElementById("output3").innerHTML="" #clears previous result
    num1 = float(document.getElementById("input1").value) #get input value 
    num2 = float(document.getElementById("input2").value) #get input value

    result = num1 * num2

    display(f"Multiplication: {result}", target="output3")


def divide_num(e):
    document.getElementById("output4").innerHTML="" #clears previous result
    num1 = float(document.getElementById("input1").value) #get input value 
    num2 = float(document.getElementById("input2").value) #get input value

    result = num1 / num2

    display(f"Divide: {result}", target="output4")
