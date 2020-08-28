from src.printer import Printer
from src.resources.photo import Photo


def test_printer():
    photo = Photo({"albumId": 13,
                   "id": 234,
                   "title": "accusamus beatae ad facilis cum similique qui sunt",
                   "url": "https://via.placeholder.com/600/92c952",
                   "thumbnailUrl": "https://via.placeholder.com/150/92c952"})

    assert Printer.display(photo) == "[234] accusamus beatae ad facilis cum similique qui sunt"
