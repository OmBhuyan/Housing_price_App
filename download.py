from flask import Flask, render_template
import boto3

app = Flask(__name__)

s3 = boto3.resource("s3")
my_bucket = s3.Bucket("mle-exploration")

@app.route("/")

def contents():
    cont = show()
    return render_template("index.html", files=cont)

def show():
    add = []
    # Output the bucket names
    for my_bucket_object in my_bucket.objects.all():
        add.append(my_bucket_object.key)
    return add

if __name__ == "__main__":

    app.run(host="0.0.0.0", port="8085", debug=True)
