from django.http import JsonResponse
import datetime



# Create your views here.
def get_endpoint_data(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')
    current_day =datetime.datetime.utcnow().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    github_file_url = "https://github.com/Luckyjnr/Hng_Task1/blob/master/core/views.py"
    github_repo_url = "https://github.com/Luckyjnr/Hng_Task1/tree/master"

    response_data = {
        "slack_name": slack_name,
        "current_day":current_day,
        "utc_time": utc_time,
        "track":track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }
    return JsonResponse(response_data)
