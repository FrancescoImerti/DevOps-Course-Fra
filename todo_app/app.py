from flask import Flask, render_template, request, redirect
from todo_app.data.session_items import get_items, add_item, delete_item, get_item, save_item
from todo_app.flask_config import Config
from todo_app.data.trello_items import TrelloManager

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    cards= TrelloManager.get_trello_cards()
    return render_template('index.html', items=sorted(cards, key= lambda x : x['status']))

@app.route('/add-item', methods=['POST'])
def add_new_item():    
    TrelloManager.add_trello_card(request.form.get('field_name'))
    return redirect('/')

@app.route('/update-item', methods=['POST'])
def update_item_status():
    card_id = request.form.get('id_to_edit')
    TrelloManager.mark_card_as_complete(card_id)
    return redirect('/')



if __name__ == '__main__':
    app.run(use_reloader=True, threaded=True)
