import os


class File_Manager:
    def __init__(self, path):
        """
        Class constructor
        :param path:
        """
        self.path = path

    def __check_path(self):
        """
        Checks if path exists
        :return: boolean
        """
        if os.path.isdir(self.path):
            return True
        else:
            return False

    def __get_files(self):
        """
        Gets each file full path given a files path
        :return: list
        """
        if self.__check_path():
            files = []
            for r, d, f in os.walk(self.path):
                for file in f:
                    if file.__contains__('.txt'):
                        file_path = os.path.join(r, file)
                        files.append(file_path)
            return files
        else:
            print('[INFO] Path is not correct')

    @staticmethod
    def __read_file(file_path):
        """
        Reads a file and returns its content
        :param file_path:
        :return: string
        """
        file_content = ''
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        return file_content

    def extract_data_from_files(self):
        """
        given an initial path in the constructor, returns a list with the files content
        :return: list
        """
        files = self.__get_files()
        file_data = []
        for file in files:
            content = self.__read_file(file)
            file_data.append(content)
        return file_data

    def get_file_count(self):
        """
        Returns the number of files in a path
        :return: integer
        """
        files = self.__get_files()
        return len(files)