var lengthOfLongestSubstring = function(s:string):number {
    let strings : string[] = []
    let currentLetters: any = [s[0]]
    let currentString = s[0]

    for (let i=1; i< s.length; i++){
        if (currentLetters.includes(s[i])){
            strings.push(currentLetters.join(''))
            currentLetters = []
            currentString = ''
            continue
        }
        currentString +=s[i]
        currentLetters.push(s[i])
    }

    let maxt_string = strings.sort((a, b) => b.length - a.length)[0]
    return maxt_string.length
};