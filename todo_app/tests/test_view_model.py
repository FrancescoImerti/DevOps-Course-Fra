"""Test module to test ViewModel class"""
import pytest

from todo_app.data.view_model import ViewModel


@pytest.fixture
def items():
    return [{'name': 'item1', 'id': "abc1", 'status': 'To do'},
            {'name': 'item2', 'id': "abc2", 'status': 'To do'},
            {'name': 'item3', 'id': "abc3", 'status': 'Doing'},
            {'name': 'item4', 'id': "abc4", 'status': 'Done'},
            ]


def test_view_model_done_property(items):
    # arrange
    model_view = ViewModel(items)

    # act
    done_items = model_view.done_items

    # assert
    expected = [{'name': 'item4', 'id': "abc4", 'status': 'Done'},]

    assert len(done_items) == 1
    assert done_items == expected


def test_view_model_doing_property(items):
    # arrange
    model_view = ViewModel(items)

    # act
    doing_items = model_view.doing_items

    # assert
    expected = [{'name': 'item3', 'id': "abc3", 'status': 'Doing'},]

    assert len(doing_items) == 1
    assert doing_items == expected


def test_view_model_to_do_property(items):
    # arrange
    model_view = ViewModel(items)

    # act
    to_do_items = model_view.to_do_items

    # assert
    expected = [{'name': 'item1', 'id': "abc1", 'status': 'To do'},
                {'name': 'item2', 'id': "abc2", 'status': 'To do'},]

    assert len(to_do_items) == 2
    assert to_do_items == expected
