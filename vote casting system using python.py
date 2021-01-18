from tkinter import *
from matplotlib import pyplot as plt

window= Tk()


print("Welcome to the vote Booth ")
print("The election is about to Start")
print("Post:Panchayat President")


nominee_1=input("Enter the nominee 1 name : ")
nominee_2=input("Enter the nominee 2 name : ")
nominee_3=input("Enter the nominee 3 name : ")


nom_1_votes=0
nom_2_votes=0
nom_3_votes=0


voter_id = [251,252,253,254,255,256,257,258]

total_no_of_voters=len(voter_id)

while True:
    if voter_id==[]:
        print("voting session is over")
        if nom_1_votes>nom_2_votes:
            percent=(nom_1_votes/total_no_of_voters)*100
            print(nominee_1,"has won","with",percent,"% of votes")
            break
        elif nom_2_votes>nom_1_votes:
            percent = (nom_2_votes / total_no_of_voters) * 100
            print(nominee_2, "has won", "with", percent, "% of votes")
            break
        elif nom_3_votes>nom_1_votes:
            percent = (nom_3_votes / total_no_of_voters) * 100
            print(nominee_3, "has won", "with", percent, "% of votes")
            break
        elif nom_3_votes>nom_2_votes:
            percent = (nom_3_votes / total_no_of_voters) * 100
            print(nominee_3, "has won", "with", percent, "% of votes")
            break
        elif nom_1_votes>nom_3_votes:
            percent=(nom_1_votes/total_no_of_voters)*100
            print(nominee_1,"has won","with",percent,"% of votes")
            break
        elif nom_2_votes>nom_3_votes:
            percent = (nom_2_votes / total_no_of_voters) * 100
            print(nominee_2, "has won", "with", percent, "% of votes")
            break
    else:
        voter = int(input("Enter your voter id no : "))
        Age = int(input("Enter your age : "))
        if Age >= 18:
            print("you are Eligible to vote")
            if voter in voter_id:
                print("you are a voter")
                voter_id.remove(voter)
                vote = int(input("Enter your vote 1 or 2 or 3 : "))
                if vote == 1:
                    nom_1_votes += 1
                    print("Thankyou for casting your valuable vote")
                elif vote == 2:
                    nom_2_votes += 1
                    print("Thankyou for casting your valuable vote")
                elif vote == 3:
                    nom_3_votes += 1
                    print("Thankyou for casting your valuable vote")

            else:
                print(" But you are not a voter here or you have already voted")
        else:
            print("Sorry! you are under Age and you are not Eligible to vote")



A=[]
B=[]
C=[]

x=((nom_1_votes/total_no_of_voters)*100)
y=((nom_2_votes /total_no_of_voters)*100)
z=((nom_3_votes /total_no_of_voters)*100)

A.append(x)
B.append(y)
C.append(z)
print(A)
print(B)
print(C)

def chart():
    plt.bar(["Nominee1"],A, width=0.3,label="Nominee_1",color='green')
    plt.bar(["Nominee2"], B, width=0.3,label="Nominee_2", color='blue')
    plt.bar(["Nominee3"], C, width=0.3,label="Nominee_3", color='purple')
    plt.legend()
    plt.ylabel('percentage of votes')
    plt.title('POLL RESULT')
    plt.show()

B1 = Button(window,text="click", fg="blue", command=chart)
B1.place(x=120,y=100)

B1.pack()
window.mainloop()
