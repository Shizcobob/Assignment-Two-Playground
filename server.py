from flask import Flask, render_template 

app = Flask(__name__)   

@app.route('/play')
@app.route('/play/<int:num>')
@app.route('/play/<int:num>/<string:colo>')         
def play(num=3, colo="blue"):
    return render_template('index.html', htmlnum=num, htmlcolo=colo)
    




if __name__=="__main__":   
    app.run(debug=True)   
