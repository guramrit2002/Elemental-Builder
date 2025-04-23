from .models import Page
from .constants import PUBLISHED_URL

def get_saved_html(page_id):
    try:
        page = Page.objects.get(id=page_id)
        print(page)
        return True, page.html
    except Exception as e:
        print(e)
        return False, str(e)

def get_error_html(error):
    return f'''<h1> Sorry for inconvinience </h1>
                <p> we are facing following issue </p>
                <p> {error} <p>'''
                
def get_data(data):
    try:
        # data.update({"created_by":data.get("created_by")})
        return data
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"errors": str(e)}

def get_published_url(project_id):
    try:
        return PUBLISHED_URL + project_id
    except Exception as e:
        import traceback
        traceback.print_exc()
        return {"errors": str(e)}