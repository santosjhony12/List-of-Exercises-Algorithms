import tkinter as tk

root = tk.Tk()

def bloquear_interface():
    root.config(cursor="watch")
    # Aqui você pode adicionar a lógica para bloquear a interação com a interface do usuário

def desbloquear_interface():
    root.config(cursor="")
    # Aqui você pode adicionar a lógica para desbloquear a interação com a interface do usuário

botao_bloquear = tk.Button(root, text="Bloquear", command=bloquear_interface)
botao_bloquear.pack()

botao_desbloquear = tk.Button(root, text="Desbloquear", command=desbloquear_interface)
botao_desbloquear.pack()

root.mainloop()
