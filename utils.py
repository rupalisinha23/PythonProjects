class processText:
    """
    All the pre processing, creation of indexes and search of the words in the documents are defined here.
    """


    def readFile(self, path):
        """
        Method to read each text file.
        :param path: defines the name of the file.
        :return: contents of the file in string type
        """
        return open(path, 'r+', encoding='utf-8').read().strip('\n')


    def create_index(self, mapping_dict, inverted_index, unique_words):
        """
        creates the inverted index which is a dictionary where the key is unique word and corresponding
        value is a list of documents where the key is present.
        :param mapping_dict: a mapping dictionary where the key is a filename and its corresponding value
                             is the contents of the file.
        :param inverted_index: it is a blank dictionary passed.
        :param unique_words: list of vocabluary present in all of the files.
        :return: inverted_index
        """
        for key, value in mapping_dict.items():
            for w in unique_words:
                if w in value:
                    if w not in inverted_index:
                        inverted_index[w] = [key]
                    else:
                        inverted_index[w].append(key)
        return inverted_index


    def search_doc(self, words, inverted_index):
        """
        User is asked to feine some words separated by white space which he/she wants to retrieve documents of.
        :param words: words defined by the user separated by white space
        :param inverted_index: inverted index as returned by the create_index method
        :return: None
        """
        w = words.strip('\n').split(' ')

        for item in w:
            if item in inverted_index:
                print('{} is present in '.format(item) + str(' '.join(inverted_index[item])) +' document(s)')
            else:
                print('{} is not present in any of the documents.'.format(item))

        return