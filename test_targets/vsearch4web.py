#!/usr/bin/python3

from flask import Flask, render_template, request, escape

# Database access context manager

app = Flask(__name__)

app.config['dbconfig'] = { 'host' : '127.0.0.1',
                           'user' : 'vsearch',
                           'password' : 'vsearchpasswd',
                           'database' : 'vsearchlogDB' }

def log_request(req: 'flask_request', res: str) -> None:
    """ Log details of the web request and the results. """
    pass



@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = ''
    log_request(request, results)
    return render_template('results.html',
                            the_title = title,
                            the_phrase = phrase,
                            the_letters = letters,
                            the_results = results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                            the_title = 'Welcome to realbadbytes vowel search')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """ Display the log contents in HTML """
    return render_template('viewlog.html',
                            the_title = 'View Log',
                            the_row_titles = titles,
                            the_data = contents,)


if __name__ == '__main__':
    app.run(debug=True)





