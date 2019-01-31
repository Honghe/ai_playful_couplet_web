from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    # if request.method == 'GET':
    #     couplet_left = request.args.get('couplet')
    #     print('couplet_left {}'.format(couplet_left))
    #     if couplet_left:
    #         return render_template('index.html', couplet_left=couplet_left, couplet_right='三四')
    #     else:
    #         return render_template('index.html')
    if request.method == 'GET':
        return render_template('index_post.html')
    elif request.method == 'POST':
        couplet_left = request.form.get('couplet')
        if couplet_left:
            return render_template('index_post.html', couplet_left=couplet_left, couplet_right='三四', placeholder=couplet_left)
        else:
            return render_template('index_post.html')

if __name__ == '__main__':
    app.run()
