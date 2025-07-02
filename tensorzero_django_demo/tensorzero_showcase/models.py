from django.db import models
from django.utils import timezone
import json


class TensorZeroInference(models.Model):
    """Store inference results from TensorZero"""
    created_at = models.DateTimeField(default=timezone.now)
    model_name = models.CharField(max_length=200)
    prompt = models.TextField()
    response = models.TextField()
    inference_id = models.CharField(max_length=100, blank=True, null=True)
    function_name = models.CharField(max_length=100, default='chat')
    temperature = models.FloatField(default=0.7)
    max_tokens = models.IntegerField(default=1000)
    metadata = models.JSONField(default=dict, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.model_name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"


class TensorZeroFeedback(models.Model):
    """Store feedback for TensorZero inferences"""
    inference = models.ForeignKey(TensorZeroInference, on_delete=models.CASCADE, related_name='feedbacks')
    created_at = models.DateTimeField(default=timezone.now)
    metric_name = models.CharField(max_length=100)
    value = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Feedback for {self.inference.inference_id}: {self.metric_name}={self.value}"


class ModelComparison(models.Model):
    """Store comparisons between different models"""
    created_at = models.DateTimeField(default=timezone.now)
    prompt = models.TextField()
    models_compared = models.JSONField(default=list)  # List of model names
    results = models.JSONField(default=dict)  # Dict of model_name: response
    winner = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Comparison {self.created_at.strftime('%Y-%m-%d %H:%M')} - {len(self.models_compared)} models"
