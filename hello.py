from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def send_to_db(data):
    with open("database.txt", mode = 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email}, {subject}, {message}')


def send_to_csv(data):
    with open("database.csv", mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=':', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        send_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Somthing wromg, try again...'



if __name__ == "__main__":
    app.run(debug=True)
