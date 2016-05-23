func longest_word(text: String) -> (String) {
    
    var tempTxt = text
    
    tempTxt += " "
    
    var word = ""
    var length = 0
    
    var max = 0
    var longestWord = ""
    
    for character in tempTxt.characters {
        if character == " " {
            if length > max {
                max = length
                longestWord = word
            }
            word = ""
            length = 0
        } else {
            word += "\(character)"
            length += 1
        }
    }
    return longestWord
}
