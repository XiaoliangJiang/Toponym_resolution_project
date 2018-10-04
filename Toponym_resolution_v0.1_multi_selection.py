import re

def subset_training_data(data, size=100, full=False):
    """
    This function aims to subset data in a smaller one as testing set.
    :param data: input data
    :param size: the size of subset
    :param full: set True to get full size of data.
    :return: the subset
    """
    subset = list()
    count = 0
    for i in data:
        # if count == 0:
        #     count += 1
        #     continue
        subset.append(i)
        count += 1
        if count > size and full is False:
            break
    return subset


def get_info(data):
    """

    :param data:
    :return:
    """
    info_set = list()
    for i in data:
        info_set.append([i.split("\t")[0], i.split("\t")[1], i.split("\t")[2]])
    return info_set


def type_judge(data, keyword):
    """

    :param data:
    :param keyword:
    :return:
    """

    if isinstance(keyword, str):
        #output_text+=("\n====================================================================\nKeyword: %s" % keyword)
        print(
            "\n====================================================================================================\nKeyword: %s" % keyword)
        # result_set+="\n====================================================================================================\nKeyword: %s" % keyword
        multi_match(data, keyword)
    elif isinstance(keyword, list):
        for i in keyword:
            #output_text+=(
            #    "\n====================================================================\nKeyword: %s" % i)
            print(
                "\n====================================================================================================\nKeyword: %s" % i)
            # result_set+="\n====================================================================================================\nKeyword: %s" % i
            multi_match(data, i)
    else:
        print("Invalid keyword input.")


def multi_match(data, keyword):
    """

    :param data:
    :param keyword:
    :return:
    """
    index_total = 0
    output_text = str()
    for i in data:
        index_total+=1
        if bool(re.search(keyword, i[2], re.IGNORECASE)):
            sentence_found = str()
            index = 0
            sentence_set = i[2].split(".")
            for j in sentence_set:
                if bool(re.search(keyword, j, re.IGNORECASE)):
                    index += 1
                    sentence_found += "\t" + str(index) + ". " + str.lstrip(j) + ".\n"
                else:
                    continue
            PMID = i[0].split(":")[1]
            output_text+="Index:%s PMID:%s, Title: %s\nSentence:\n%s\n" % (index_total,PMID, i[1], sentence_found)
            #print("Index:%s ID:%s, Title: %s\nSentence:\n%s" % (index_total,i[0], i[1], sentence_found))
        else:
            if bool(re.search(keyword, i[1], re.IGNORECASE)):
                PMID = i[0].split(":")[1]
                output_text += "Index:%s PMID:%s, Title: %s\nSentence:\n\tNone. The keyword is only in the Title.###\n\n" % (
                index_total, PMID, i[1])
            pass
    with open("{}_Toponym_Output.txt".format(keyword), "w") as file:
        file.write(output_text)
    # return

def main():
    """

    :return:
    """
    #with open('/Users/xiaoliang/Downloads/abstracts.tsv', 'r') as f:
    with open('/Users/xiaoliang/Desktop/Study/2018FALL/PhD/Research/Lebanon_result.txt', 'r') as f:
        f1 = subset_training_data(f, full=True)  # 15,544,339
    # keywords = ["London", "New York", "Boston", "Lebanon", "Manchester", "Paris", "Berlin", "Washington", "Beijing",
    #             "Taizhou"]
    keywords = ["Lebanon"]
    type_judge(get_info(f1), keywords)
    import os
    os.getcwd()

if __name__ == '__main__':
    main()
