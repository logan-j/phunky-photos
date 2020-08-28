class Printer:
    @staticmethod
    def display(photo):
        return "[{id}] {title}".format(id=photo.id, title=photo.title)
