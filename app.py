from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app=Flask(__name__)

@app.route("/")
@app.route("/index")

def index():
    con = sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from livro")
    data=cur.fetchall()
    return render_template ("index.html", datas=data)

@app.route("/add_livro", methods=["POST", "GET"])
def add_livro():
    if request.method == "POST":
        titulo = request.form["titulo"]
        autor = request.form["autor"]
        ano = request.form["ano"]

        con = sql.connect("form_db.db")
        cur = con.cursor()
        cur.execute("insert into livro(TITULO,AUTOR,ANO) values (?,?,?)", (titulo, autor, ano))
        con.commit()
        flash("O Livro foi registrado ", "success")
        return redirect(url_for("index"))
    return render_template("add_livro.html")

@app.route("/edit_livro/<string:id>", methods=["POST","GET"])
def edit_livro(id):
    if request.method=="POST":
        titulo=request.form["titulo"]
        autor=request.form["autor"]
        ano=request.form["ano"]
        con=sql.connect("form_db.db")
        cur=con.cursor()
        cur.execute("update livro set TITULO=?,AUTOR=?,ANO=? where ID=?", (titulo,autor,ano,id))
        con.commit()
        flash("O Livro foi atualizado", "success")
        return redirect(url_for("index"))
    con=sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from livro where ID =?", (id,))
    data=cur.fetchone()
    return render_template("edit_livro.html", datas=data)



@app.route("/delete_livro/<string:id>", methods=["GET"])
def delete_livro(id):
    con=sql.connect("form_db.db")
    cur=con.cursor()
    cur.execute("delete from livro where ID=?", (id,))
    con.commit()
    flash("Livro deletado", "warning")
    return redirect(url_for("index"))

@app.route("/pesquisar_livro", methods=["POST"])
def pesquisar_livro():
    titulo=request.form["titulo"]
    con = sql.connect("form_db.db")
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute("select * from livro where TITULO = ?", (titulo))
    data=cur.fetchall()
    return render_template ("pesquisar_livro.html", datas=data)


if __name__=='__main__':
    app.secret_key="admin123"
    app.run(debug=True)