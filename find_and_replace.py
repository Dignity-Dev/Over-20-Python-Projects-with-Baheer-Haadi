def replace_word():
    
    content = "Welcome to python programming, in this lesson lesson we we will talk on find and replace"
    word_to_find = input("Find What: ")
   
    replace_with = input( "Enter replacement: ")
    print(str.replace(word_to_find, replace_with))
   


replace_word()