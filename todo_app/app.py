from flask import Flask, render_template, request, redirect
from todo_app.data.session_items import get_items, add_item, delete_item, get_item, save_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', items=sorted(get_items(), key= lambda x : x['status']))

@app.route('/add-item', methods=['POST'])
def add_new_item():    
    add_item(request.form.get('field_name'))
    return redirect('/')

@app.route('/update-item', methods=['POST'])
def update_item_status():
    item = get_item(request.form.get('id_to_edit'))
    item["status"] = 'Completed'  
    save_item(item)
    return redirect('/')

@app.route('/remove-item', methods=['POST'])
def remove_item():    
    delete_item(request.form.get('id_to_remove'))
    return redirect('/')



if __name__ == '__main__':
    app.run(use_reloader=True, threaded=True)
