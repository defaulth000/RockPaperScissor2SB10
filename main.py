import random

def rock_paper_scissors():
 user = input ("Pedra, Papel ou Tesoura?")
 computer = random.choice(['pedra', 'papel', 'pesoura'])
 print(f"Defalt escolheu {computer}")

 if user == computer:
   return "Empate!"   
   
 elif (user == "pedra" and computer == "tesoura" or (user == "papel" and computer == 
 "pedra")) or (user == "tesoura" and computer == "papel"):    
   return "Você é o foda!"
   
 else:
   
    return "Vive de aluguel agora!"

print(rock_paper_scissors())