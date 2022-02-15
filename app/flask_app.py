from flask import Flask, request, session

import elozza_text_assets
from elozza import elozza_response

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "wepoifjeaoiferh"


# ====================
@app.route("/", methods=["GET", "POST"])
def adder_page():
    # Set up session variable to store dialogue history
    if "dialogue" not in session:
        session["dialogue"] = []
    if request.method == "POST":
        question = str(request.form["question"])
        # If the question field is not empty, add the question and response
        # to the dialogue history
        if question:
            session["dialogue"].append(f'YOU: {question}<br>' +
                                       f'ELOZZA: {elozza_response(question)}')
            if len(session["dialogue"]) > 5:
                session["dialogue"] = session["dialogue"][-5:]
            session.modified = True
    return f'''
        <html>
            <head>
                <link rel="stylesheet" link href="/static/css/base.css">
            </head>
            <body onLoad="document.getElementById('question').focus();">
                <pre>{elozza_text_assets.title}</pre>
                <p>{elozza_text_assets.blurb}</p>
                <p>Ask ELOZZA a question:</p>
                <form method="post" action=".">
                    <div class="row" style="width: 100%">
                        <input name="question" id="question" />
                        <input type="submit" value="Ask" id="ask" />
                    </div>
                    <p>{'<br><br>'.join(session["dialogue"])}</p>
                </form>
            </body>
            ''' + '''
            <script>
            if ( window.history.replaceState ) {
              window.history.replaceState( null, null, window.location.href );
            }
            </script>
        </html>
    '''
