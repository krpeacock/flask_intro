from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cruds', methods=["GET"])
def index():
  return render_template('index.html', cruds=cruds_list)

@app.route('/cruds', methods=["POST"])
def create():
  new_crud = Crud(request.form['crud_name'])
  cruds_list.append(new_crud)

  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True, port=3000)
