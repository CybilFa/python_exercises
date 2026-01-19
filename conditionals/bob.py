def answers(text):
    text = text.strip()

    if not text:
         return "Fine. Be that way!"

    is_question = text.endswith("?")
    is_yelling = text.isupper()
    
    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    
    if is_yelling:
        return  "Whoa, chill out!"
    if is_question:
        return "Sure."

    return "Whatever."
  

print(answers("Hey how are you?"))
print(answers("WHY YOU DOIN THIS?"))
print(answers("   ")) 

      