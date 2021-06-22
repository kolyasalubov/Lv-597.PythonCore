from flask_bootstrap import Bootstrap
from flask import Flask
from flask import render_template
from my_bs_manager import BaseManager as my_manager



app = Flask(__name__)
bootstrap = Bootstrap(app)


base = 'score.db'

sql = """
    SELECT name, round((correct/questions),2) as Score
    FROM leaderboard
    ORDER BY correct DESC, Score DESC
    """



def show_score():
    with my_manager(base) as bm:
        bm.execute(sql)
        result = bm.fetchall()
    res_dict={}
    #res_dict={}.fromkeys([i[1] for i in result], 0)
    for i in result:
        res_dict[i[0]] = i[1]
    return res_dict



@app.route('/')
def start():
    main_result = show_score()
    return render_template('index.html', main_result=main_result)



if __name__ == '__main__':
    app.run(debug=True)
