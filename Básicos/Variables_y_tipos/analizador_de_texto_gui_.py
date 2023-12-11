import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, scrolledtext
from tkinter import font as tkFont
import tkinter.scrolledtext as scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def contar_caracter_gui(texto):
    caracter = simpledialog.askstring("Contar Carácter", "Ingrese el caracter que desea contar:")
    if caracter:
        contador = texto.count(caracter)
        messagebox.showinfo("Resultado", f"El caracter '{caracter}' aparece {contador} veces en el texto.")

def invertir_texto_gui(texto):
    texto_invertido = texto[::-1]
    messagebox.showinfo("Texto Invertido", texto_invertido)

def extraer_texto_gui(texto):
    def extraer_por_palabra():
        palabra_extraer = simpledialog.askstring("Extraer Palabra", "Ingrese la palabra que desea extraer:")
        if palabra_extraer:
            indice = texto.find(palabra_extraer)
            if indice != -1:
                extracto = texto[indice:indice+len(palabra_extraer)]
                messagebox.showinfo("Texto Extraído", extracto)
            else:
                messagebox.showwarning("Resultado", "Palabra no encontrada")

    def extraer_por_indices():
        inicio = simpledialog.askinteger("Índices de Inicio", "Índice de inicio:")
        fin = simpledialog.askinteger("Índices de Fin", "Índice de fin:")
        if inicio is not None and fin is not None:
            extracto = texto[inicio:fin]
            messagebox.showinfo("Texto Extraído", extracto)

    ventana_extraer = tk.Toplevel()
    ventana_extraer.title("Extraer Texto")

    boton_palabra = tk.Button(ventana_extraer, text="Extraer por Palabra", command=extraer_por_palabra)
    boton_palabra.pack()

    boton_indices = tk.Button(ventana_extraer, text="Extraer por Índices", command=extraer_por_indices)
    boton_indices.pack()

def reemplazar_caracteres_gui(texto):
    caracter_a_reemplazar = simpledialog.askstring("Reemplazar Carácter", "Ingrese el caracter que desea reemplazar:")
    nuevo_caracter = simpledialog.askstring("Nuevo Carácter", "Ingrese el nuevo caracter:")
    if caracter_a_reemplazar and nuevo_caracter:
        texto_reemplazado = texto.replace(caracter_a_reemplazar, nuevo_caracter)
        messagebox.showinfo("Texto Reemplazado", texto_reemplazado)

def cifrado_cesar_gui(texto):
    desplazamiento = simpledialog.askinteger("Cifrado César", "Ingrese el desplazamiento para el cifrado César:")
    if desplazamiento is not None:
        texto_cifrado = ""
        for caracter in texto:
            if caracter.isalpha():
                ascii_offset = 65 if caracter.isupper() else 97
                indice = (ord(caracter) - ascii_offset + desplazamiento) % 26
                caracter_cifrado = chr(indice + ascii_offset)
                texto_cifrado += caracter_cifrado
            else:
                texto_cifrado += caracter
        messagebox.showinfo("Texto Cifrado", texto_cifrado)

def analisis_frecuencia_caracteres(texto):
    frecuencia = {}
    for caracter in texto:
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            frecuencia[caracter] = 1
    return frecuencia

def grafico_frecuencia_caracteres_gui(texto):
    frecuencia = analisis_frecuencia_caracteres(texto)
    frecuencias_ordenadas = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)

    caracteres, frecuencias = zip(*frecuencias_ordenadas)

    fig, ax = plt.subplots()
    ax.bar(caracteres, frecuencias)

    ax.set_xlabel('Caracteres')
    ax.set_ylabel('Frecuencia')
    ax.set_title('Frecuencia de Caracteres en el Texto (Ordenada)')

    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    canvas.draw()

def crear_ventana_principal():
    global ventana, text_input

    ventana = tk.Tk()
    ventana.title("Analizador de Texto")
    
    estilo = ttk.Style(ventana)
    estilo.theme_use('clam')  # 'alt', 'clam', 'classic', 'default', 'vista'

    fuente_normal = tkFont.Font(family="Helvetica", size=12)
    color_fondo = '#f0f0f0'
    color_botones = '#e1e1e1'
    ventana.configure(bg=color_fondo)

    frame_texto = tk.Frame(ventana, bg=color_fondo)
    frame_texto.pack(fill='both', expand=True, padx=10, pady=10)

    label = tk.Label(frame_texto, text="Ingrese su texto aquí:", bg=color_fondo, font=fuente_normal)
    label.pack()
    text_input = scrolledtext.ScrolledText(frame_texto, height=10, font=fuente_normal)
    text_input.pack(fill='both', expand=True)

    estilo.configure('TButton', font=fuente_normal, background=color_botones)

    frame_botones = ttk.Frame(ventana)
    frame_botones.pack(fill='x', padx=10, pady=10)

    boton_contar = ttk.Button(frame_botones, text="Contar Caracteres", command=lambda: contar_caracter_gui(text_input.get("1.0", "end-1c")))
    boton_contar.pack(side='left', padx=5)

    boton_contar = ttk.Button(frame_botones, text="Contar Caracteres", command=lambda: contar_caracter_gui(text_input.get("1.0", "end-1c")))
    boton_contar.pack(side='left', padx=5)

    boton_invertir = ttk.Button(frame_botones, text="Invertir Texto", command=lambda: invertir_texto_gui(text_input.get("1.0", "end-1c")))
    boton_invertir.pack(side='left', padx=5)

    boton_reemplazar = ttk.Button(frame_botones, text="Reemplazar Caracteres", command=lambda: reemplazar_caracteres_gui(text_input.get("1.0", "end-1c")))
    boton_reemplazar.pack(side='left', padx=5)

    boton_cifrar = ttk.Button(frame_botones, text="Cifrado César", command=lambda: cifrado_cesar_gui(text_input.get("1.0", "end-1c")))
    boton_cifrar.pack(side='left', padx=5)

    boton_frecuencia = ttk.Button(frame_botones, text="Análisis de Frecuencia", command=lambda: grafico_frecuencia_caracteres_gui(text_input.get("1.0", "end-1c")))
    boton_frecuencia.pack(side='left', padx=5)

    boton_salir = ttk.Button(frame_botones, text="Salir", command=ventana.quit)
    boton_salir.pack(side='left', padx=5)

    ventana.mainloop()

crear_ventana_principal()