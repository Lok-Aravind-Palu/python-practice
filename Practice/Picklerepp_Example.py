import pickle


class PickleExample(object):
    something = {1: "1", 2: "2", 3: "f"}

    @staticmethod
    def open_file(file_name):

        f = open(file_name, "wb")
        return f

    @staticmethod
    def file_close(file_name):
        file_name.close()

    def convert_to_pickle(self, file_name):
        pickle.dump(self.something, file_name)

    @classmethod
    def read_file(cls, file_name):
        f = open(file_name, "rb")
        return f

    @staticmethod
    def convert_back_to_object(file_name):
        example_dict = pickle.load(file_name)
        return example_dict


if __name__ == '__main__':
    file = PickleExample().open_file("pickle_example")
    PickleExample().convert_to_pickle(file)
    PickleExample().file_close(file)

    file = PickleExample.read_file("pickle_example")
    ex = PickleExample().convert_back_to_object(file)
    PickleExample().file_close(file)
    print(ex[2])
