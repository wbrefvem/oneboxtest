from rest_framework_xml.renderers import XMLRenderer
import xmltodict
from dicttoxml import dicttoxml


class OneBoxXMLRenderer(XMLRenderer):

    def render(self, data, media_type=None, renderer_context=None):
        ret = super(OneBoxXMLRenderer, self).render(data, media_type, renderer_context)

        print dicttoxml(xmltodict.parse(ret)['root'])

        return ret
