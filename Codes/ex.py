from flask import Flask, render_template,request
app=Flask(__name__)
@app.route("/")
def first():
    return render_template('first.html')
@app.route("/encrypt")
def encrypt():
    return render_template('encrypt.html')
@app.route("/decrypt")
def decrypt():
    return render_template('decrypt.html')
@app.route("/enc")
def encryption():
    text=request.args.get('text')
    key=int(request.args.get('key'))
    l='abcdefghijklmnopqrstuvwxyz'
    u=l.upper()
    ct=''
    for c in text:
        if c in l:
            ct+=l[(l.find(c)+key)%26]
        elif c in u:
            ct+=u[(u.find(c)+key)%26]
    return render_template('result.html',msg=ct)
@app.route("/dec")
def decryption():
    text=request.args.get('text')
    key=int(request.args.get('key'))
    l='abcdefghijklmnopqrstuvwxyz'
    u=l.upper()
    pt=''
    for c in text:
        if c in l:
            pt+=l[(l.find(c)-key)%26]
        elif c in u:
            pt+=u[(u.find(c)-key)%26]
    return render_template('result1.html',msg1=pt)
@app.route("/result")
def result():
    return render_template('result.html')
@app.route("/result1")
def result1():
    return render_template('result1.html')
if __name__=="__main__":
    app.run(debug=True)
