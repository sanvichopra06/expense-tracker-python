from flask import Flask, render_template, request, redirect
#imports Flask so you can use it.
app = Flask(__name__) #creates your web application.
expenses =[]
#decorater- which URL should run this function? that's where a decorator comes in.
@app.route("/", methods= ["POST", "GET"]) 
#"GET" — when someone opens the website.
# "POST" — when someone submits the expense form.
def home():
    
    if request.method == "POST":
        amount = int(request.form["amount"])
        category = request.form["category"]
        description = request.form["description"]
        expense = {
                    "amount" : amount,
                    "category" : category,
                    "description" : description
                }
        expenses.append(expense)
    total = 0
    for expense in expenses:
        total += expense["amount"] 

    cat_expenses = {}
    for i in expenses:
        cat_expenses[i["category"]] = cat_expenses.get(i["category"], 0) + i["amount"]
        
    return render_template("index.html", expenses= expenses, total= total, cat_expenses= cat_expenses)

if __name__ == "__main__": #"If this Python file is being run directly, execute the code inside this block."
    #it helps the server to not start unexpectedly
    app.run() #starts the local server