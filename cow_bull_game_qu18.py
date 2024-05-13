import random;


def Check_num(guess,random_number):
    Points=[0,0];
    for i in range(len(guess)):
        if guess[i] == random_number[i]:
            Points[0] +=1;
        else:
            Points[1]+=1;
    return Points; 


def Guess_num(Chances):
    guess=input("Guess a number\n");
    if len(guess) != 4:
        print("please enter a valid 4 digit number\n");
        Guess_num(Chances);
    Chances+=1;
    return guess,Chances;


if  __name__ == "__main__":
    replay='y';
    while replay:
        Chances=0;
        random_number=str(random.randint(1000,9999));
        print(random_number);
        guess,Chances=Guess_num(Chances);
        while guess != random_number:
            Points=Check_num(guess,random_number);
            print(Points[0]," : Cows\n",Points[1]," : Bulls");
            guess,Chances=Guess_num(Chances);
        print("Yayy you won the game in ",Chances ,"chances do you want to play again >> \n");    
        replay=input("press y to play again\n");