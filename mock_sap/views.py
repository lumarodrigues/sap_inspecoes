from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def ordem_inspecao(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Recebido no mock SAP:", data)
            return JsonResponse({"status": "sucesso", "message": "Ordem de inspeção recebida"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método não permitido"}, status=405)
