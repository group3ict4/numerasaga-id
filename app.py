from flask import Flask, render_template, redirect,request
coins = 10
app = Flask(__name__)
posts = []


# HOME
@app.route('/')
def home():
    return render_template('index.html')

# SISWA
@app.route('/siswa')
def siswa():

    global coins

    return render_template(
        'siswa.html',
        coins=coins
    )
# GURU
@app.route('/guru')
def guru():
    return render_template('guru.html')

@app.route("/login-guru")
def login_guru():
    return render_template("login_guru.html")


# REGISTER GURU
@app.route("/register-guru")
def register_guru():
    return render_template("register_guru.html")


# GAME SNAKE
@app.route('/snake-game')
def snake_game():
    return render_template('snake_game.html')

@app.route('/materi')
def materi():
    return render_template('materi.html')

@app.route('/ruang-curhat')
def ruang_curhat():

    global coins

    if coins >= 10:

        return redirect(
        'https://wa.me/6283829704809'
        )

    return render_template(
        'belum_cukup.html',
        coins=coins
    )
@app.route('/add-coin')
def add_coin():

    global coins

    coins += 10

    return 'OK'
@app.route("/modul")
def modul():
    return render_template("modul.html")

@app.route("/bank-soal")
def bank_soal():
    return render_template("bank_soal.html")

# RUANG BERBAGI
@app.route("/ruang-berbagi", methods=["GET", "POST"])
def ruang_berbagi():

    if request.method == "POST":

        nama = request.form["nama"]
        isi = request.form["postingan"]

        post_baru = {
            "nama": nama,
            "isi": isi,
            "like": 0,
            "komentar": []
        }

        posts.append(post_baru)

        return redirect("/ruang-berbagi")

    return render_template(
        "ruang_berbagi.html",
        posts=posts
    )
# LIKE POST
@app.route("/like/<int:index>")
def like(index):

    posts[index]["like"] += 1

    return redirect("/ruang-berbagi")
# KOMENTAR POST
@app.route("/komentar/<int:index>", methods=["POST"])
def komentar(index):

    isi_komentar = request.form["komentar"]

    posts[index]["komentar"].append(isi_komentar)

    return redirect("/ruang-berbagi")

if __name__ == '__main__':
    app.run(debug=True)