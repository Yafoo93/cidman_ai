from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
import os

@method_decorator(csrf_exempt, name='dispatch')
class LegalSearchView(View):
    def post(self, request):
        body = json.loads(request.body)
        query = body.get("query", "").lower()

        # Load constitution.json
        path = os.path.join(settings.BASE_DIR, "static", "data", "constitution.json")
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        results = []

        for chapter in data.get("content", []):
            for section in chapter.get("sections", []):
                section_title = section.get("title", "")
                section_content = section.get("content", "")

                if query in section_title.lower() or query in section_content.lower():
                    results.append({
                        "chapter": chapter.get("chapter"),
                        "section_number": section.get("section_number"),
                        "section_title": section_title,
                        "section_content": section_content
                    })

                for subsection in section.get("subsections", []):
                    if query in subsection.get("content", "").lower():
                        results.append({
                            "chapter": chapter.get("chapter"),
                            "section_number": section.get("section_number"),
                            "section_title": section_title,
                            "subsection_number": subsection.get("subsection_number"),
                            "subsection_content": subsection.get("content")
                        })

        return JsonResponse({"query": query, "results": results})