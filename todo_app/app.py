"""flask application"""
from flask import Flask, render_template, request, redirect
from todo_app.flask_config import Config
from todo_app.data.trello_items import TrelloManager
from todo_app.data.view_model import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items = TrelloManager.get_trello_cards()
        item_view_model = ViewModel(items)
        return render_template('index.html', view_model=item_view_model)
        # return render_template('index.html', items=sorted(cards, key= lambda x : x['status']))

    @app.route('/add-item', methods=['POST'])
    def add_new_item():    
        TrelloManager.add_trello_card(request.form.get('field_name'))
        return redirect('/')

    @app.route('/update-item', methods=['POST'])
    def update_item_status():
        card_id = request.form.get('id_to_edit')
        TrelloManager.mark_card_as_complete(card_id)
        return redirect('/')
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(use_reloader=True, threaded=True)
