import string;
import random;


def random_pass(password):
    password_list=list(password);
    random.shuffle(password_list);
    # final=''.join(password_list)
    # return final;
    return password_list

def random_seq(n):
    A=[]
    x=random.choice(range(1,4));
    y=random.choice(range(1,3));
    z=random.choice(range(1,int((n-(x+y))/2)))
    w=n-(x+y+z)
    A.append(x)
    A.append(y)
    A.append(z)
    A.append(w)
    return A;
    


def pass_weak(alpha_low,alpha_up,num,special_char):
    random_small=[random.choice(alpha_low) for _ in range(3)];
    random_up=[random.choice(alpha_up) for _ in range(1)];
    random_char=[random.choice(special_char) for _ in range(1)];
    random_num=[str(random.choice(num)) for _ in range(3)];
    weak_pass=random_small+random_up+random_char+random_num;
    return weak_pass;


def pass_gen(alpha_low,alpha_up,num,special_char,choice,n):

    A=random_seq(n);
    
    random_small=[random.choice(alpha_low) for _ in range(A[3])];
    random_up=[random.choice(alpha_up) for _ in range(A[1])];
    random_char=[random.choice(special_char) for _ in range(A[2])];
    random_num=[str(random.choice(num)) for _ in range(A[0])];
    
    password=random_small+random_up+random_char+random_num;

    if choice == 'hard':
        password=random_pass(password);
    return password;



alpha_low=list(string.ascii_lowercase);
alpha_up=list(string.ascii_uppercase);
num=list(range(0,10));
special_chars = ['#', '$', '%', '&', '*', '(', ')', '-', '+', '=', '_', '{', '}', '|', '!', '\"', '?', '/'];
repeat='y';

while repeat == 'y':
    choice=input('How strong password do you want ??? \nWeak\nStrong\nHard\n');

    match choice:
        case 'weak':
            password=pass_weak(alpha_low,alpha_up,num,special_chars);
            print("Your ",choice," password is \n" , password);
        case 'strong':
            password=pass_gen(alpha_low,alpha_up,num,special_chars,choice,9);
            password_2=pass_gen(alpha_low,alpha_up,num,special_chars,choice,10);
            print("Your ",choice," password is \n",password,' or \n',password_2);
        case 'hard':
            password=pass_gen(alpha_low,alpha_up,num,special_chars,choice,11);
            password_2=pass_gen(alpha_low,alpha_up,num,special_chars,choice,12);
            print("Your ",choice," password is \n",password,'or \n',password_2);
        case _:
            print("Enter the correct value");
    repeat=input("do you want to generate password again ??\ny\nn");
print("Thanks for using this password generator !!!!");
