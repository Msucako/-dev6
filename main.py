from flask import Flask, render_template,request
import random
import string

app = Flask(__name__)

facts_list=["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
"2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.","Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir."]

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>  <a href='/2'>Rastgele gerçekler! </a>  <a href='/Deneme'>Diğer sayfa </a>"
    


@app.route("/Deneme")
def main():
    return "<h1>Ronaldo'mu,Messi'mi</h1>"

           

@app.route("/2")
def main_1():
     return f'<p>{random.choice(facts_list)}</p>'


@app.route("/3")
def birleştir():
    return render_template("index.html")

#Şifre Oluşturucu Bölümü
@app.route("/4")
def rastgele():
    return render_template('index1.html')

@app.route('/generate_password', methods=['POST'])
def generate():
    password_length = int(request.form['password_length'])
    generated_password = generate_password(password_length)
    return render_template('index.html', password=generated_password)


        



if __name__ == '__main__':
    app.run(debug=True)
