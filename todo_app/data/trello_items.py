# This code uses the 'requests' library to call trello API
# http://docs.python-requests.org
import requests
import os

list_ids = {"to_do":"6501688a993cb949a6478d07",
            "doing":"6501688bc072b227f990762d",
            "done":"6501688a1c964b99f5ea6d20"
}


class TrelloManager:
  
    board_id = os.environ.get('BOARD_ID')
    APIKey = os.environ.get('TRELLO_API_KEY')
    APIToken = os.environ.get('TRELLO_TOKEN')
    url = f"https://api.trello.com/1/boards/{board_id}/lists"


    @classmethod
    def get_trello_cards(cls):
        """
        function used to list all trello cards
        """
    
        url = f"https://api.trello.com/1/boards/{TrelloManager.board_id}/lists"

        query = {
        'key': TrelloManager.APIKey,
        'token': TrelloManager.APIToken,
        'cards':'open',
        'card_fields':['id','name', 'idList']
        }

        response = requests.request("GET", url, params=query)

        response_json = response.json()
        print(response_json)
        cards = []
        for trello_list in response_json:
            for card in trello_list['cards']:
                card['status'] = trello_list['name']
                cards.append(card)

        return cards
    

    @staticmethod
    def add_trello_card(title):
        """
        Adds a new item with the specified title to the session.
        Args:
            title: The title of the item.

        Returns:
            item: The saved item.
        """
        url = f"https://api.trello.com/1/cards"
        
        querystring = {"name": title, "idList": list_ids["to_do"], "key": TrelloManager.APIKey, "token": TrelloManager.APIToken}
        response = requests.request("POST", url, params=querystring)

        return 


    @staticmethod
    def mark_card_as_complete(card_id):
        """
        API put call to change status of a card to complete
        """

        url = f"https://api.trello.com/1/cards/{card_id}"
        print(url)
        query = {
        'key': TrelloManager.APIKey,
        'token': TrelloManager.APIToken,
        'idList': list_ids['done']
        }

        response = requests.request("PUT", url, params=query)

        return


