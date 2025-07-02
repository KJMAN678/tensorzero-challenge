from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import TensorZeroInference, TensorZeroFeedback, ModelComparison
from tensorzero import TensorZeroGateway
import json
import logging
import traceback
from datetime import datetime

logger = logging.getLogger(__name__)


def index(request):
    """Main page showing TensorZero capabilities"""
    recent_inferences = TensorZeroInference.objects.all()[:10]
    context = {
        'recent_inferences': recent_inferences,
        'available_models': [
            'openai::gpt-4o-mini',
            'anthropic::claude-3-haiku-20240307',
            'mistral::mistral-small-latest',
        ]
    }
    return render(request, 'tensorzero_showcase/index.html', context)


def inference_demo(request):
    """Demo page for single model inference"""
    if request.method == 'POST':
        model_name = request.POST.get('model_name', 'openai::gpt-4o-mini')
        prompt = request.POST.get('prompt', '')
        temperature = float(request.POST.get('temperature', 0.7))
        max_tokens = int(request.POST.get('max_tokens', 1000))
        
        try:
            # For demo purposes, we'll simulate TensorZero responses
            # In a real deployment, you would use:
            # with TensorZeroGateway.build_http(gateway_url="http://localhost:3000") as client:
            #     response = client.inference(...)
            
            # Simulated response
            response_text = f"[Simulated {model_name} Response]\n\n{prompt}\n\nThis is a simulated response. To use real TensorZero, you need to:\n1. Deploy TensorZero Gateway\n2. Configure your models\n3. Update this view with actual gateway URL"
            
            # Save to database
            inference = TensorZeroInference.objects.create(
                model_name=model_name,
                prompt=prompt,
                response=response_text,
                temperature=temperature,
                max_tokens=max_tokens,
                metadata={'demo': True}
            )
            
            messages.success(request, 'Inference completed successfully!')
            return redirect('inference_detail', pk=inference.pk)
            
        except Exception as e:
            logger.error(f"Inference error: {str(e)}\n{traceback.format_exc()}")
            messages.error(request, f'Error during inference: {str(e)}')
    
    return render(request, 'tensorzero_showcase/inference_demo.html')


def model_comparison(request):
    """Compare responses from multiple models"""
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        models = request.POST.getlist('models')
        
        results = {}
        for model in models:
            # Simulated responses for demo
            results[model] = f"[{model} Response]\n{prompt}\n\nThis would be the actual response from {model}."
        
        comparison = ModelComparison.objects.create(
            prompt=prompt,
            models_compared=models,
            results=results
        )
        
        return redirect('comparison_detail', pk=comparison.pk)
    
    return render(request, 'tensorzero_showcase/model_comparison.html')


def inference_detail(request, pk):
    """Show details of a specific inference"""
    inference = TensorZeroInference.objects.get(pk=pk)
    return render(request, 'tensorzero_showcase/inference_detail.html', {'inference': inference})


def comparison_detail(request, pk):
    """Show details of a model comparison"""
    comparison = ModelComparison.objects.get(pk=pk)
    return render(request, 'tensorzero_showcase/comparison_detail.html', {'comparison': comparison})


@csrf_exempt
def feedback_api(request, inference_id):
    """API endpoint for submitting feedback"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            inference = TensorZeroInference.objects.get(pk=inference_id)
            
            feedback = TensorZeroFeedback.objects.create(
                inference=inference,
                metric_name=data.get('metric_name', 'rating'),
                value=float(data.get('value', 0)),
                comment=data.get('comment', '')
            )
            
            return JsonResponse({'status': 'success', 'feedback_id': feedback.pk})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


def analytics(request):
    """Show analytics and insights from TensorZero usage"""
    total_inferences = TensorZeroInference.objects.count()
    model_usage = {}
    
    for inference in TensorZeroInference.objects.all():
        model_name = inference.model_name
        if model_name not in model_usage:
            model_usage[model_name] = 0
        model_usage[model_name] += 1
    
    context = {
        'total_inferences': total_inferences,
        'model_usage': model_usage,
        'recent_feedback': TensorZeroFeedback.objects.all()[:10]
    }
    
    return render(request, 'tensorzero_showcase/analytics.html', context)
