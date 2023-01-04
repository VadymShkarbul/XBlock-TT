import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, String
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin


class NewXBlock(XBlock, StudioEditableXBlockMixin):
    title = String(
        default="Block title",
        help="Enter block title here",
    )
    content_field = String(
        default="Block content",
        scope=Scope.content,
        help="Enter block content here",
    )

    editable_fields = ("title", "content_field")

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        loader = ResourceLoader("newblock")
        data = dict(title=self.title, content=self.content_field)
        template = loader.render_django_template(
            "static/html/newblock.html", context=data
        )
        frag = Fragment(template)
        frag.add_css(self.resource_string("static/css/newblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/newblock.js"))
        frag.initialize_js('NewXBlock')
        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("NewXBlock",
             """<newblock/>
             """),
            ("Multiple NewXBlock",
             """<vertical_demo>
                <newblock/>
                <newblock/>
                <newblock/>
                </vertical_demo>
             """),
        ]
