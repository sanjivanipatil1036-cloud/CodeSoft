
import tkinter as tkr
import random

root = tkr.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.config(bg="#F8F8FF")

user_score = 0
comp_score = 0
choices = ["Rock", "Paper", "Scissors"]

def play(choice):
    global user_score, comp_score
    computer = random.choice(choices)
    result = ""

    if choice == computer:
        result = "It's a Tie!"
    elif (choice == "Rock" and computer == "Scissors") or \
         (choice == "Scissors" and computer == "Paper") or \
         (choice == "Paper" and computer == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        comp_score += 1

    user_choice_label.config(text=f"You chose: {choice}")
    comp_choice_label.config(text=f"Computer chose: {computer}")
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_choice_label.config(text="")
    comp_choice_label.config(text="")
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")

title_label = tkr.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="#F8F8FF")
title_label.pack(pady=15)

frame = tkr.Frame(root, bg="#F8F8FF")
frame.pack(pady=10)

rock_btn = tkr.Button(frame, text="Rock", width=10, bg="#FFB6C1", command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tkr.Button(frame, text="Paper", width=10, bg="#90EE90", command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tkr.Button(frame, text="Scissors", width=10, bg="#ADD8E6", command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

user_choice_label = tkr.Label(root, text="", font=("Arial", 12), bg="#F8F8FF")
user_choice_label.pack(pady=5)

comp_choice_label = tkr.Label(root, text="", font=("Arial", 12), bg="#F8F8FF")
comp_choice_label.pack(pady=5)

result_label = tkr.Label(root, text="", font=("Arial", 14, "bold"), fg="#333", bg="#F8F8FF")
result_label.pack(pady=10)

score_label = tkr.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#F8F8FF")
score_label.pack(pady=10)

reset_btn = tkr.Button(root, text="Reset", bg="#FFD580", command=reset_game, width=12)
reset_btn.pack(pady=5)

footer_label = tkr.Label(root, text="Created by Sanjivani Patil | CODSOFT", font=("Arial", 8), bg="#F8F8FF", fg="gray")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
