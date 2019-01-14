import markovify
import pronouncing
import re
import sys

def is_rhyming(my_word_1, my_word_2):
    # print("w1: {} w2: {} ", my_word_1, my_word_2)
    try:
        is_a_rhyme = (my_word_1 in pronouncing.rhymes(my_word_2))
    except:
        print("is_rhyming failed. w1: {} w2: {} ", my_word_1, my_word_2)

    return is_a_rhyme

def rhyme_possibilities(word):
    # print(pronouncing.rhymes(word))
    return len(pronouncing.rhymes(word))

def get_sample_sentence_last():
    sentence_1 = text_model.make_short_sentence(200)
    # sentence_1 = text_model.make_sentence()
    sentence_1 = re.sub(r'[^a-zA-Z0-9 ]', '', sentence_1) + "."
    word_1 = sentence_1.split()[-1]
    word_1 = word_1[:-1]
    return (sentence_1, word_1)





if __name__ == '__main__':
    # file_name = "Kanye West"
    # file_name = "Drake"
    # file_name = "Nirvana"
    file_name = "Rihanna"
    # file_name = "trump_walkout"
    # file_name = "myNirvana"
    # file_name = "silverstein"
    # file_name = "trump_speeches"
    file_name = "corpora/" + file_name + ".txt"
    with open(file_name) as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text, state_size=2)

    # print("Sentences:")
    # for i in range(5):
        # print "\t" + re.sub(r'[^a-zA-Z0-9 ]', '', text_model.make_sentence()) + "."
        # print text_model.make_sentence()

    # print("Tweets:")
    # for i in range(5):
    #     print("\t" + text_model.make_short_sentence(140))

    # generate line 1:
    # paragraph = []
    # sentence_1 = text_model.make_sentence()
    # paragraph.append(sentence_1)
    # print("\t" + sentence_1)
    # if len(sentence_1) < 1:
    #     print("Corpus cannot generate a sentence")
    #     exit()
    # last_word = sentence_1.split()[-1]

    # sys.exit()
    for i in range(8):
        sentence_1, word_1 = get_sample_sentence_last()
        new_sentence, new_last = get_sample_sentence_last()

        trial_number = 1
        while (not rhyme_possibilities(word_1)):
            if trial_number < 3:
                sentence_1, word_1 = get_sample_sentence_last()
                print("no rhymes for: " + word_1)
                trial_number = trial_number + 1
            else:
                print("Trial 3 no rhymes: " + word_1)
                sys.exit()

        trial_number = 1
        while (not rhyme_possibilities(new_last)):
            if trial_number < 3:
                new_sentence, new_last = get_sample_sentence_last()
                print("no rhymes for: " + new_last)
                trial_number = trial_number + 1
            else:
                print("Trial 3 no rhymes: " + new_last)
                sys.exit()

        # print("sent1: \t" + sentence_1)
        # print("last1: " + word_1)
        # print("sent2: \t" + new_sentence)
        # print("last2: " + new_last)

        trial_number = 1
        while(not is_rhyming(new_last, word_1)):
            if trial_number > 3:
                sentence_1, word_1 = get_sample_sentence_last()
                trial_number = 1
                # sys.exit()
            new_sentence, new_last = get_sample_sentence_last()
            # print("w1: {} w2: {}", sentence_1, new_sentence)
            trial_number = trial_number + 1
        print(sentence_1)
        print("\t" + new_sentence + "\n")
