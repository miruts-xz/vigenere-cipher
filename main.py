import tkinter as tk
from vigenere_cipher import *

window = tk.Tk(className="Vigenere cipher")

combo_box_frame = tk.Frame()

label_top_frame = tk.Frame()
text_top_frame = tk.Frame()

button_middle_frame = tk.Frame()
key_middle_frame = tk.Frame()
label_bottom_frame = tk.Frame()
text_bottom_frame = tk.Frame()


def sel():
    s = type.get()
    if s == 0:
        button['text'] = "Encrypt Message"
        output_label['text'] = "Encrypted output"
    else:
        button['text'] = "Decrypt Message"
        output_label['text'] = "Decrypted output"


combo_box = tk.Radiobutton(master=combo_box_frame)
type = tk.IntVar()
encrypt = tk.Radiobutton(combo_box_frame, text="Encrypt", variable=type, value=0, command=sel)
decrypt = tk.Radiobutton(combo_box_frame, text="Decrypt", variable=type, value=1, command=sel)
encrypt.pack(side=tk.LEFT)
decrypt.pack(side=tk.LEFT)
prompt_label = tk.Label(text="Enter Message: ", master=label_top_frame)
input_field = tk.Text(master=label_top_frame, height=5, width=45)
key_label_field = tk.Label(text="Enter key: ", master=key_middle_frame)
key_input_field = tk.Entry(master=key_middle_frame, width=40)
output_label = tk.Label(text="Encrypted output", master=label_bottom_frame)
output_field = tk.Label(master=label_bottom_frame, height=5, width=50)
prompt_label.pack(side=tk.LEFT)
input_field.pack(side=tk.LEFT)
output_label.pack(side=tk.LEFT)
output_field.pack(side=tk.LEFT)


def handle_encrypt():
    cipher_key: str = key_input_field.get()
    cipher_key = cipher_key.replace(" ", "")
    cipher_key = cipher_key.upper()
    raw_message = input_field.get("1.0", tk.END)
    raw_message = raw_message.replace(" ", "")
    raw_message = raw_message.upper()
    raw_message = raw_message.strip(' \n\t')
    cipher_k = generate_key(raw_message, cipher_key)
    if type.get() == 0:
        cipher_t = encrypt_message(raw_message, cipher_k)
    else:
        cipher_t = decrypt_message(raw_message, cipher_k)
    output_field['text'] = cipher_t


button = tk.Button(text="Encrypt Message", master=key_middle_frame, command=handle_encrypt)
key_label_field.pack(side=tk.LEFT)
key_input_field.pack(side=tk.LEFT)
button.pack()
combo_box_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
label_top_frame.grid(row=1, column=0, padx=5, pady=5)
text_top_frame.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

key_middle_frame.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

label_bottom_frame.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

window.mainloop()
