
import stripe
from django.conf import settings
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse


stripe.api_key = settings.STRIPE_SECRET_KEY

@method_decorator(csrf_exempt, name='dispatch')
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'T-shirt',
                    },
                    'unit_amount': 2000,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success/',
            cancel_url='http://localhost:8000/cancel/',
        )
        return JsonResponse({'stripe_url': session.url})






@csrf_exempt
def stripe_webhook(request):
    if request.method != "POST":
        return HttpResponse("This endpoint only accepts POST requests.", status=405)

    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')  # ❗ Always use .get()

    if not sig_header:
        return HttpResponse("Missing Stripe Signature Header", status=400)

    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(f"⚠️ Invalid payload: {e}", status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(f"❌ Signature verification failed: {e}", status=400)

    # ✅ Successfully verified
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print("✅ Payment succeeded:", session)

    return HttpResponse(status=200)


# "C:\Users\Foysal Munna\Downloads\stripe_1.28.0_windows_x86_64\stripe.exe" login
# stripe listen --forward-to localhost:8000/stripe/webhook/  (local host ar link dete hobe )
# stripe trigger checkout.session.completed  (for checkout completed command)