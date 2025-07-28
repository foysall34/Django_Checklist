import datetime

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # শুধু login API এর জন্য লগ করবো
        if request.path == "/auth/api/login/":
            log_time = datetime.datetime.now()
            method = request.method
            path = request.path
            ip = request.META.get('REMOTE_ADDR')
            
            try:
                body = request.body.decode('utf-8')  # body কে string এ convert করলাম
            except:
                body = "<unable to decode body>"

            log_line = f"[{log_time}] {method} {path} from {ip}\nBody: {body}\n"

            print(log_line)  # Terminal এ দেখাবে

            # চাইলে ফাইলেও লিখতে পারো
            with open("login_api_log.txt", "a") as f:
                f.write(log_line)

        response = self.get_response(request)
        return response
