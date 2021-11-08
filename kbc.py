### KBC [KON BANEGA CROREPATI]
QNS=[
     ['Which of one these sounds would associated with the heart?','Dhak Dhak'],
     ["In the Ramyana,which demon impersonated rama's voice,screeming,'Lakshman! help me?",'Marich'],
     ['Which one of these cards would you associate the phrase Aam Aadmi Adhikar?','Aadhar card'],
     ['The sasural of which of these international sports persons from India in Pakistan?','Saina mirza'],
     ['Which of these words pharases was famously used in many of his dialogues by actor "Pran"?',"Barkhurdaar"],
     ['Which of these is a term for a place where people gather for sayri and gazal?','Mushaira'],
     ['In the Mughal Era,which of these harbours was also known as Babul Mecca and Meccaidwar?','Surat'],
     ['After whom is the annual award,given by the Govt of India to an outstanding handloom weaver named?','Saint Kabir'],
     ['Damascus is the capital of which country?','Syria'],
     ['Which is the largest banana producing country in the world?','India'],
     ['Which of these words mean "water"?','Varun'],
     ['Which gas is most reactive of all chemical elements?','Fluorine'],
     ['Which of these sports man started cariar as attraviling ticket examiner with Indian Railway?','Mahendra Singh Dhoni'],
     ['Which is the coldest place in India?','Drass']
    ]
ANS=[
     ['Tring Tring', 'Tap Tap','Click click','Dhak Dhak'],
     ['Surpanakha','Khora','Marich','Dushana'],
     ['Pan card','Voter card','Aadhar card','Ration card'],
     ['Siana nehwal','Saina mirza','Anisa sayyed','Anjum chopra'],
     ['Khamosh','Barkhurdaar','Jaani','Babu mosai'],
     ['Rukhsar','Mushaira','Shikara','Mahabara'],
     ['Bharuch','Surat','Porbandar','Khambal'],
     ['Acharya vinoba bhave','Saint Kabir','Mahatma Gandhi','Gul ahmed'],
     ['Tunisia','Jordan','Syria','Lebanon'],
     ['Brazil','India','Mexico','China'],
     ['Rahul','Suraj','Varun','Rajiv'],
     ['Oxigen','Chlorine','Fluorine','Hydrogen'],
     ['Bhuvneshwar kumar','Shekhar dhavan','Ravindra jadeja','Mahendra Singh Dhoni'],
     ['Yusmarg','Kulgam','Drass','Leh']
    ]
print('     :: WELCOME TO KBC ::')
m=[]
lifeline=True
exit=True
for i in range(len(QNS)):
    if i+1==1:
        price=1000
    elif i+1<=3:
        price+=2000
    elif i+1<14:
        price*=2
    else:
        price=f'{70000000} crore'
    if exit==False:
        print('Wrong answer you are out of the game!')
        break
    else:
        print(f'{i+1}.{QNS[i][0]}')
        for j in range (len(ANS[i])):
            print(f'\t{j+1}.{ANS[i][j]}')
            if j+1==4:
                if lifeline==True:
                    print('You have one lifeline ==> 50-50')
                    opt=int(input('Enter your option/5050:-'))
                    if opt==5050:
                        s=[]
                        for p in range(len(ANS[i])):
                            if len(s)!=2:
                                if ANS[i][p]!=QNS[i][1]:
                                    s.append(ANS[i][p])
                            else:
                                break
                        for t in range(2):
                            ANS[i].remove(s[t])
                        for u in range(len(ANS[i])):
                            print(f'\t{u+1}.{ANS[i][u]}')
                        ans=int(input('Enter your option:-'))
                        if ANS[i][ans-1]==QNS[i][1]:
                            print('\nRight answer\n you won ',price,'rupees\n')  
                            i+=1
                            lifeline=False;
                        else:
                            print('\nInvalid input!')
                            exit=False
                    elif opt==1 or opt==2 or opt==3 or opt==4:
                        if ANS[i][opt-1]==QNS[i][1]:
                            print('\nRight answer\nyou won',price,'rupees\n')
                            i+=1
                        else:
                            exit=False
                    else:
                        print('\nInvalid input!')
                        exit=False                               
                else:
                    opt=int(input('Enter your option:-'))
                    if opt==1 or opt==2 or opt==3 or opt==4:
                        if ANS[i][opt-1]==QNS[i][1]:
                            print('\nRight answer\nyou won',price,'rupees\n')
                            i+=1
                        else:
                            exit=False
                    else:
                        print('\nInvalid input!')
                        exit=False
print('\tTHANK YOU')

