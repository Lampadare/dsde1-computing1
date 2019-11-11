def concatenate_sentences(sentence1, sentence2):
    
    while sentence1[0] == ' ':
        del sentence1[0]
    while sentence1[-1] == ' ':
        del sentence1[-1]


    condition_1_one = sentence1[0].isupper()                
    if ((sentence1[-1] == '.' or '!' or '?') and (condition_1_one == True)):                   
        print('YesOneYes')
    else:
        print('NoOneNo')
        raise ValueError
    



    while sentence2[0] == ' ':
        del sentence2[0]
    while sentence2[-1] == ' ':
        del sentence2[-1]


    condition_1_two = sentence2[0].isupper()                  #Checks two starts with uppercase
    if sentence2[-1] == '.' or '!' or '?':                    #Checks two ends with punctuation
        condition_2_two = True
    else:
        condition_2_two = False
    
    if condition_1_two and condition_2_two == True:           #Checks TWO respects all conditions
        two = 'yes'
    else:
        two = 'no'
        raise ValueError

    return print(sentence1+' '+sentence2)
