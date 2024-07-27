import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None

# take data in from csv file and put it into two list French and english words
try:
    data = pandas.read_csv('study_words.csv')
except FileNotFoundError:
    data = pandas.read_csv('data/french_words.csv')
# french_words = data['French'].to_list()
# english_words = data["English"].to_list()
word_dic = data.to_dict(orient='records')
chosen_word = word_dic[0]


# button actions
def new_flashy():
    global chosen_word
    global word_dic
    canvas.itemconfig(canvas_image, image=front_image)
    random_int = random.randint(0, 99)
    chosen_word = random.choice(word_dic)
    french_word = chosen_word['French']
    canvas.itemconfig(card_title, text=f"French", fill='black')
    canvas.itemconfig(card_word, text=f"{french_word}", fill='black')
    global timer
    try:
        window.after_cancel(timer)
    except ValueError:
        timer = window.after(3000, back, chosen_word)
    finally:
        timer = window.after(3000, back, chosen_word)


def green_button():
    global chosen_word
    global word_dic
    word_dic.remove(chosen_word)
    df = pandas.DataFrame(word_dic)
    df.to_csv('study_words.csv')
    new_flashy()


def back(flash_card):
    canvas.itemconfig(canvas_image, image=back_image)
    english_word = flash_card['English']
    canvas.itemconfig(card_title, text=f"English", fill='white')
    canvas.itemconfig(card_word, text=f"{english_word}", fill='white')
    # print(english_word)


# def back():
#     canvas.itemconfig(canvas_image, image=back_image)

# window set up
window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# canvas setup
canvas = tkinter.Canvas(width=800, height=526, highlightthickness=0)
front_image = tkinter.PhotoImage(file='./images/card_front.png')
back_image = tkinter.PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text='Title', fill='black', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='trouve', fill='black', font=('Ariel', 60, 'italic'))
canvas.grid(column=0, row=0, columnspan=2)
# Buttons

my_image = tkinter.PhotoImage(file='images/right.png')
right_button = tkinter.Button(image=my_image, command=green_button)
right_button.grid(column=1, row=1)

other_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=other_image, command=new_flashy)
wrong_button.grid(column=0, row=1)

# start the flash cards
new_flashy()
window.mainloop()
#pumy vnsc kkpa szse

