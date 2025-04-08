from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt
import json


def profile_page(request, username):
    profile = get_object_or_404(UserProfile, username=username)
    return render(request, 'profile.html', {'profile': profile})


def get_profile_api(request, username):
    try:
        profile = UserProfile.objects.get(username=username)
        data = {
            "name": profile.name,
            "designation": profile.designation,
            "email": profile.email,
            "phone": profile.phone,
            "address": profile.address,
            "linkedin": profile.linkedin,
            "image": profile.image.url if profile.image else "",
            "company_link": profile.company_link
        }
        return JsonResponse(data)
    except UserProfile.DoesNotExist:
        return JsonResponse({"error": "Profile not found"}, status=404)


@csrf_exempt
def create_profile_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            profile = UserProfile.objects.create(
                username=data["username"],
                name=data["name"],
                designation=data["designation"],
                email=data["email"],
                phone=data["phone"],
                address=data["address"],
                linkedin=data["linkedin"],
                company_link=data["company_link"],
                image=data.get("image", "")  # Optional field
            )

            return JsonResponse({"message": "Profile created successfully!"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
