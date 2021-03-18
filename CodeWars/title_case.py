def title_case(title, minor_words=""):
    titled = ""
    for word in title.split(" "):
        if not titled:
            titled += "{0} ".format(word.capitalize())
        elif word.lower() not in minor_words.lower().split(" "):
            titled += "{0} ".format(word.capitalize())
        else:
            titled += "{0} ".format(word.lower())
    return titled.rstrip()


title_case('')
title_case('a clash of KINGS', 'a an the of')
title_case('THE WIND IN THE WILLOWS', 'The In')
title_case('the quick brown fox')





