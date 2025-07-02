from django.contrib import admin
from .models import TensorZeroInference, TensorZeroFeedback, ModelComparison

# Register your models here.

@admin.register(TensorZeroInference)
class TensorZeroInferenceAdmin(admin.ModelAdmin):
    list_display = ['inference_id', 'model_name', 'prompt_preview', 'created_at']
    list_filter = ['model_name', 'created_at']
    search_fields = ['prompt', 'response', 'inference_id']
    readonly_fields = ['inference_id', 'created_at']
    
    def prompt_preview(self, obj):
        return obj.prompt[:50] + '...' if len(obj.prompt) > 50 else obj.prompt
    prompt_preview.short_description = 'プロンプト'

@admin.register(TensorZeroFeedback)
class TensorZeroFeedbackAdmin(admin.ModelAdmin):
    list_display = ['inference', 'metric_name', 'value', 'created_at']
    list_filter = ['metric_name', 'created_at']
    search_fields = ['inference__inference_id']

@admin.register(ModelComparison)
class ModelComparisonAdmin(admin.ModelAdmin):
    list_display = ['id', 'prompt_preview', 'created_at']
    list_filter = ['created_at']
    search_fields = ['prompt']
    
    def prompt_preview(self, obj):
        return obj.prompt[:50] + '...' if len(obj.prompt) > 50 else obj.prompt
    prompt_preview.short_description = 'プロンプト'
