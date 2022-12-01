from zookeeper import ZooKeeper


class Zoo:
    """
    Will be composed of Animal/ZooKeeper instances
    """

    def __init__(self, name, location):
        self.animals = list()
        self.zookeepers = list()
        pass

    def add_animal(self, animal):
        pass

    def add_zookeeper(self, zookeeper):
        pass
