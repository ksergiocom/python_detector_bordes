import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
im = Image.open('cameraman.png').convert('L')
I = np.array(im, dtype=np.float32)

rows, cols = I.shape

# Creamos matrices para los gradientes (inicializadas a 0)
Gx = np.zeros((rows, cols), dtype=np.float32)
Gy = np.zeros((rows, cols), dtype=np.float32)

# ------------------------------------------------------
# Gradiente horizontal (dirección x): diferencia con el píxel izquierdo
for i in range(rows):
    for j in range(1, cols):    # empezamos en j=1 porque necesitamos el píxel de la izquierda
        Gx[i, j] = I[i, j] - I[i, j-1]

# ------------------------------------------------------
# Gradiente vertical (dirección y): diferencia con el píxel de abajo
for i in range(rows-1):         # hasta rows-1 porque necesitamos el píxel inferior
    for j in range(cols):
        Gy[i, j] = I[i, j] - I[i+1, j]

# ------------------------------------------------------
# El valor númerico del gradiente (total) se calcula como la raiz cuadrada de la suma de los cuadrados de los dos gradientes previos, para cada pixel.
grad_mag = np.sqrt(Gx**2 + Gy**2)

# ------------------------------------------------------
# original + magnitud
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(I, cmap='gray')
plt.title('Imagen original (grises)')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(grad_mag, cmap='gray')
plt.title('Magnitud del gradiente')
plt.axis('off')

plt.tight_layout()
plt.savefig('original_y_gradiente.png', dpi=150, bbox_inches='tight')
plt.close()

# ------------------------------------------------------
# varios umbrales
umbral = [5, 10, 20, 30, 40, 50, 80, 120]

plt.figure(figsize=(15, 10))
for idx, th in enumerate(umbral):
    bordes = (grad_mag > th).astype(np.uint8) * 255
    
    plt.subplot(2, 4, idx+1)
    plt.imshow(bordes, cmap='gray')
    plt.title(f'Umbral = {th}')
    plt.axis('off')

plt.suptitle('Diferentes umbrales - Detector con bucles')
plt.tight_layout()
plt.savefig('umbrales_varios.png', dpi=150, bbox_inches='tight')
plt.close()