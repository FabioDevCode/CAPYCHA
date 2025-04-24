from captcha.image import ImageCaptcha # type: ignore
import random
import string
import base64
import io

def generate_captcha(length=6, width=200, height=70, font_sizes=(42, 50, 56)):
    # Générer le texte aléatoire
    characters = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choices(characters, k=length))

    # Créer le générateur d'image
    image_captcha = ImageCaptcha(width=width, height=height, fonts=None, font_sizes=font_sizes)

    # Générer l'image
    image = image_captcha.generate_image(captcha_text)

    # Convertir en base64 pour usage dans un JSON
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return captcha_text, img_base64
