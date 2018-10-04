# original_data=pd.read_csv('abstracts.tsv',sep="\t") # Error1: Expected 3 fields in line 2058836, saw 4


def subset_training_data(data, size=1000):
    """

    :param data:
    :param size:
    :return:
    """
    subset = list()
    count = 0
    for i in data:
        if count == 0:
            count += 1
            continue
        subset.append(i)
        count += 1
        if count > size:
            break
    return subset


def get_abstracts(data):
    """
    get the abstracts from the third column in original data
    :param data: input data (3 columns: id, title, sentences)
    :return: all of the abstracts.
    """
    abstracts = list()
    for i in data:
        abstracts.append(i.split("\t")[2])
    # print(len(abstracts))
    return abstracts


#
# abstracts = get_abstracts(original_data)
# len(abstracts) # 15,544,339


def get_IDs(data):
    """
    get the IDs from the third column in original data
    :param data: input data (3 columns: id, title, sentences)
    :return: all of the IDs.
    """
    IDs = list()

    for i in data:
        IDs.append(i.split("\t")[0])
    # print(len(IDs))
    return IDs


# IDs = get_IDs(original_data)
# len(IDs) #

def get_titles(data):
    """
    get the abstracts from the third column in original data
    :param data: input data (3 columns: id, title, sentences)
    :return: all of the titles.
    """
    titles = list()
    for i in data:
        titles.append(i.split("\t")[1])
    # print (len(titles))
    return titles


# titles = get_titles(original_data)
# len(titles)

# print(abstracts[0:100])

def finding_results(input_data, keyword):
    """
    Finding a sentences which contains a particular keywords.
    :param input_data: input data
    :param keyword: the particular keywords
    :return: the position of this keywords, or -1 for absence.
    """
    finding_results = list()
    for i in input_data:
        finding_results.append(i.find(keyword))
    return finding_results


def print_sentences(test_result, abstracts, IDs, titles):
    """

    :param test_result:
    :param abstracts:
    :param IDs:
    :param titles:
    :return:
    """
    sentences = list()
    selected_IDs = list()
    selected_titles = list()
    selected_i = list()
    for i in range(len(test_result)):
        if test_result[i] > -1:
            start_position = abstracts[i][0:test_result[i]][::-1].find(".")
            # print (start_position)
            if start_position == -1:  # Appeared in the first sentences.
                # print (abstracts[i].find("."))
                sentences.append(abstracts[i][0:(abstracts[i].find(".")) + 1])
                # print (sentences)
            else:  # Appeared in any other sentences but the first one.I'm here
                before_position = abstracts[i][0:test_result[i]][::-1].find(".")
                first_half_sentence = abstracts[i][0:test_result[i]][::-1][0:before_position][::-1]
                # first_half_sentence=abstracts[i][0:start_position][::-1][0:(abstracts[i][0:start_position][::-1].find("."))][::-1]
                # print (first_half_sentence)
                after_position = abstracts[i][test_result[i]:].find(".")
                second_half_sentence = abstracts[i][test_result[i]:][0:after_position + 1]
                sentences.append(first_half_sentence + second_half_sentence)
            selected_IDs.append(IDs[i])
            selected_titles.append(titles[i])
            selected_i.append(i)

    for i in range(0, len(sentences)):
        print("i number: %d \nID: %s, Title: %s \nSentence: %s" % (
            selected_i[i], selected_IDs[i], selected_titles[i], sentences[i]))
    return sentences


# sentences
#
# abstracts[1]


def main():
    """

    :return:
    """
    with open('/Users/xiaoliang/Downloads/abstracts.tsv', 'r') as f:
        f1 = subset_training_data(f, 10000)
    IDs = get_IDs(f1)
    titles = get_titles(f1)
    abstracts = get_abstracts(f1)
    test_result = finding_results(abstracts, keyword="Iowa")
    # print (test_result)
    print_sentences(test_result, abstracts, IDs, titles)


if __name__ == '__main__':
    main()
