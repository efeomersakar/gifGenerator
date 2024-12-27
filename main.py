from tkinter import Tk, filedialog, Button, Label
from PIL import Image


def select_images():
    global image_paths
    image_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")],
    )
    if image_paths:
        label_selected.config(text=f"{len(image_paths)} images selected.")


def create_gif():
    if not image_paths:
        label_result.config(text="No images selected.")
        return

    images = [Image.open(img) for img in image_paths]
    save_path = filedialog.asksaveasfilename(
        title="Save GIF",
        defaultextension=".gif",
        filetypes=[("GIF Files", "*.gif")],
    )

    if save_path:
        images[0].save(
            save_path,
            save_all=True,
            append_images=images[1:],
            duration=150,
            loop=0
        )
        label_result.config(text=f"GIF Kaydedildi: {save_path}")


root = Tk()
root.title("gif Generate")
root.geometry("300x150")  # Genişlik x Yükseklik
root.eval('tk::PlaceWindow . center')

image_paths = []

btn_select = Button(root, text="Resimleri Seçiniz", command=select_images)
btn_select.pack(pady=10)

label_selected = Label(root, text="Hiçbir resim seçilmedi.")
label_selected.pack()

btn_create = Button(root, text="GIF Oluştur", command=create_gif)
btn_create.pack(pady=10)

label_result = Label(root, text="")
label_result.pack()

root.mainloop()
