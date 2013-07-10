from flask import Flask, request, jsonify

app = Flask(__name__)

class Calc:
  def add(self, m, n):
    self.sum = int(m + n)
    return m + n
  def product(self, m, n):
    self.prod = m * n
    return m * n

@app.route('/calc/<int:m>&<int:n>', methods=['GET', 'POST'])
def calc(m, n):
  if request.method == 'GET':
    result = Calc()

    #json_results = []
    #d = {
    #  'sum': result.add(m, n),
    #  'product': result.product(m, n),
    #}
    #json_results.append(d)
    #return jsonify(items=json_results)

    return jsonify(
        sum = str(result.add(m, n)),
        product = str(result.product(m, n))
      )

#'sum': 1, 'product': 2,




if __name__ == "__main__":
    app.run(debug=True)
