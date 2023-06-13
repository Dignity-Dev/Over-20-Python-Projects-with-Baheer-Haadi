def replace_word():
    
    content = "Welcome to python programming, in this lesson lesson we we will talk on find and replace"
    word_to_find = input("Find What: ")
    if word_to_find not in content:
        print("word not found!")
    else:
        replace_with = input( "Enter replacement: ")
        print(content.replace(word_to_find, replace_with))
   


replace_word()