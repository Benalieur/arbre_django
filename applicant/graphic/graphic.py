import numpy as np
import matplotlib.pyplot as plt

input_simploniens = [2]*11 +[1]*5 +[3]*2  # A remplacer par un input

def get_graph(input_value: dict, username: str):
    input_simploniens = []
    for value in input_value:
        input_simploniens.append(int(input_value[value]))
    categories = ['C1', 'C2', 'C3', 'C4', 'C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','']
    print(input_simploniens)
    # le '' est la pour éviter un message d'erreur
    A1 = input_simploniens[0:2]+[0]*16
    A2 = [0]*2 + input_simploniens[3:7] + [0]*12
    A3 = [0]*7 + input_simploniens[8:14] + [0]*5
    A4 =  [0]*16 + input_simploniens[16:18]
    A5 = input_simploniens

    A1 =  [*A1, A1[0]]    #pour remplir le bord
    A2 =  [*A2, A2[0]]
    A3 =  [*A3, A3[0]]
    A4 =  [*A4, A4[0]]
    # A5 =  [*A5, A5[0]]

    label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(A1))

    plt.figure(figsize=(18, 18))
    plt.subplot(polar=True)
    plt.plot(label_loc, A1, label='E1')
    plt.plot(label_loc, A2, label='E2')
    plt.plot(label_loc, A3, label='E3')
    plt.plot(label_loc, A4, label='E4')
    #plt.plot(label_loc, A5, label='tot')

    #plt.title('Compétences', size=40)
    lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)

    plt.savefig(f"static/image/graphic/graphic_{username}.jpg")

    plt.legend()
