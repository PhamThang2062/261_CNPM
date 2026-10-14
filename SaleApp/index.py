from flask import Flask, render_template, request
import dao


app=Flask(__name__)


@app.route("/")
def index():
    cate=dao.load_categories()
    q=request.args.get("q")
    cate_id=request.args.get("cate_id")

    return render_template("index.html",cates=cate,prods=dao.load_products(q=q,cate_id=cate_id))





if __name__ == "__main__":
    app.run(debug=True)
