from django.db import models
import markdown

# Create your models here.
class MarkdownFile(models.Model):
	file = models.FileField(upload_to='markdown/')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str(self):
		return self.file.name

	def get_html(self):
		content = self.file.read().decode('utf-8')
		return markdown.markdown(content)