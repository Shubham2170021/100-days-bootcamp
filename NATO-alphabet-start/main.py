
import pandas
student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
for (index, row) in student_data_frame.iterrows():
    data_dicr={row.letter:row.code for (index,row) in student_data_frame.iterrows()}
def nato():
    user=input("Enter a word").upper()
    try:
        list=[data_dicr[letter] for letter in user ]
    except KeyError:
        print("Sorry only letter can enter")
        nato()
    else:
        print(list)

nato()


