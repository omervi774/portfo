from flask import Flask, render_template,request,url_for,redirect
import csv
app = Flask(__name__)

def write_to_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
    print(email,subject,message)
    with open('database.csv', 'a', newline='') as database:
        csv_writer = csv.writer(database, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
       

@app.route("/")
def my_home():
    return render_template('./index.html')

@app.route("/<page_name>")
def specific_page(page_name = None):
    return render_template(f'./{page_name}')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    data = request.form.to_dict()
    print(data)
    write_to_csv(data)
    return redirect('./thankyou.html')
    

    



