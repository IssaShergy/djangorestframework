from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
class Ebook(models.Model):
    titil = models.CharField(max_length = 150)
    author = models.CharField(max_length = 150)
    description = models.TextField()
    publication_date = models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self) -> str:
        return f"{self.titil}"
class Review(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    review_author = models.CharField(max_length = 8,blank=True,null=True)
    review = models.TextField()
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),
    MaxValueValidator(5)])
    Ebook=models.ForeignKey(Ebook,
                        on_delete=models.CASCADE,
                        related_name="reviews")
    def __str__(self)  :
        return str(self.rating)
    
    
    
    
    
