from string import punctuation


def word_counter(input_string):
    #clean_string = input_string.translate(str.maketrans('','',punctuation))
    clean_string = input_string.replace('-',' ')
    print(clean_string)
    word_list = clean_string.split()

    return len(set(word_list))



print(word_counter("jenkins-ci-cd-pipelines-devops-for-beginners"))