import os
import datetime
import requests
import textwrap
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from PIL import Image
from io import BytesIO

class NewsReport:
    def __init__(self, report_data):
        self.report_data = report_data
        self.timestamp = datetime.datetime.now()
        self.week = self.timestamp.strftime("%U")
        self.year = self.timestamp.strftime("%Y")
        self.folder = os.path.expanduser(f"~/Documentos/noticias/{self.week}-{self.year}")
        os.makedirs(self.folder, exist_ok=True)
        self.filepath = os.path.join(self.folder, f"{self.timestamp.strftime('%Y-%m-%d_%H-%M-%S')}.pdf")
    
    def fetch_image(self, url):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return Image.open(BytesIO(response.content))
        except Exception:
            pass
        return None
    
    def add_wrapped_text(self, c, text, x, y, max_width, line_height):
        wrapper = textwrap.TextWrapper(width=80)
        lines = wrapper.wrap(text)
        for line in lines:
            if y < 50:  
                c.showPage()
                c.setFont("Helvetica", 10)
                y = letter[1] - 50
            c.drawString(x, y, line)
            y -= line_height
        return y
    
    def generate_pdf(self):
        c = canvas.Canvas(self.filepath, pagesize=letter)
        width, height = letter
        y_position = height - 50
        
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y_position, "Relatório de Notícias")
        y_position -= 30
        
        c.setFont("Helvetica", 12)
        c.drawString(50, y_position, f"Data: {self.timestamp.strftime('%d/%m/%Y %H:%M:%S')}")
        y_position -= 30
        
        for category, articles in self.report_data.items():
            if not articles:
                continue
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, y_position, category.capitalize())
            y_position -= 20
            
            for article in articles:
                title = article.get("title", "Sem título")
                description = article.get("description", "Sem descrição disponível.")
                image_url = article.get("imageUrl")
                url = article.get("url", "")
                
                c.setFont("Helvetica-Bold", 12)
                y_position = self.add_wrapped_text(c, title, 50, y_position, max_width=500, line_height=14)
                
                c.setFont("Helvetica", 10)
                y_position = self.add_wrapped_text(c, description, 50, y_position, max_width=500, line_height=12)
                
                if image_url:
                    image = self.fetch_image(image_url)
                    if image and y_position > 200:  
                        image.thumbnail((200, 150))
                        img_buffer = BytesIO()
                        image.save(img_buffer, format="PNG")
                        c.drawImage(ImageReader(img_buffer), 50, y_position - 160, width=200, height=150)
                        y_position -= 160
                
                y_position -= 10
                c.setFont("Helvetica-Oblique", 10)
                y_position = self.add_wrapped_text(c, f"Fonte: {url}", 50, y_position, max_width=500, line_height=12)
                y_position -= 20
                
                if y_position < 100:
                    c.showPage()
                    y_position = height - 50
        
        c.save()
        print(f"Relatório salvo em: {self.filepath}")