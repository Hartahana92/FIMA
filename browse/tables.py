import django_tables2 as tables

from .models import PaperInf
from .models import MetaboliteInf
from .models import LungCancerTher
from .models import LungCancerTherPubl

from .models import BreastCancerPaper
from .models import BreastCancerMet
from .models import BreastCancerTher
from .models import BreastCancerTherPubl

from .models import KidneyCancerPaper
from .models import KidneyCancerMet
from .models import KidneyCancerTher
from .models import KidneyCancerTherPubl

from .models import ProstateCancerPaper
from .models import ProstateCancerMet
from .models import ProstateCancerTher
from .models import ProstateCancerTherPubl

from .models import DiabetesCancerPaper
from .models import DiabetesCancerMet
from .models import DiabetesCancerTher

from .models import ColorectalCancerPaper
from .models import ColorectalCancerMet
from .models import ColorectalCancerTher
from .models import ColorectalCancerTherPubl

from .models import ArthritisCancerTher
from .models import ArthritisCancerTherPubl

from .models import DepressionCancerTher
from .models import DepressionCancerTherPubl

from .models import CvdCancerTher
from .models import CvdCancerTherPubl




from .models import CvdCancerOurs

class PaperInfTable(tables.Table):
    class Meta:
        model = PaperInf
        template_name = "django_tables2/bootstrap.html"

class MetaboliteInfTable(tables.Table):
    class Meta:
        model = MetaboliteInf
        template_name = "django_tables2/bootstrap.html"

class LungCancerTherTable(tables.Table):
    class Meta:
        model = LungCancerTher
        template_name = "django_tables2/bootstrap.html"

class LungCancerTherPublTable(tables.Table):
    class Meta:
        model = LungCancerTherPubl
        template_name = "django_tables2/bootstrap.html"


class BreastCancerPaperTable(tables.Table):
    class Meta:
        model = BreastCancerPaper
        template_name = "django_tables2/bootstrap.html"

class BreastCancerMetTable(tables.Table):
    class Meta:
        model = BreastCancerMet
        template_name = "django_tables2/bootstrap.html"

class BreastCancerTherTable(tables.Table):
    class Meta:
        model = BreastCancerTher
        template_name = "django_tables2/bootstrap.html"

class BreastCancerTherPublTable(tables.Table):
    class Meta:
        model = BreastCancerTherPubl
        template_name = "django_tables2/bootstrap.html"





class KidneyCancerPaperTable(tables.Table):
    class Meta:
        model = KidneyCancerPaper
        template_name = "django_tables2/bootstrap.html"

class KidneyCancerMetTable(tables.Table):
    class Meta:
        model = KidneyCancerMet
        template_name = "django_tables2/bootstrap.html"

class KidneyCancerTherTable(tables.Table):
    class Meta:
        model = KidneyCancerTher
        template_name = "django_tables2/bootstrap.html"

class KidneyCancerTherPublTable(tables.Table):
    class Meta:
        model = KidneyCancerTherPubl
        template_name = "django_tables2/bootstrap.html"



class ProstateCancerPaperTable(tables.Table):
    class Meta:
        model = ProstateCancerPaper
        template_name = "django_tables2/bootstrap.html"

class ProstateCancerMetTable(tables.Table):
    class Meta:
        model = ProstateCancerMet
        template_name = "django_tables2/bootstrap.html"

class ProstateCancerTherTable(tables.Table):
    class Meta:
        model = ProstateCancerTher
        template_name = "django_tables2/bootstrap.html"

class ProstateCancerTherPublTable(tables.Table):
    class Meta:
        model = ProstateCancerTherPubl
        template_name = "django_tables2/bootstrap.html"



class DiabetesCancerPaperTable(tables.Table):
    class Meta:
        model = DiabetesCancerPaper
        template_name = "django_tables2/bootstrap.html"

class DiabetesCancerMetTable(tables.Table):
    class Meta:
        model = DiabetesCancerMet
        template_name = "django_tables2/bootstrap.html"

class DiabetesCancerTherTable(tables.Table):
    class Meta:
        model = DiabetesCancerTher
        template_name = "django_tables2/bootstrap.html"



class ColorectalCancerPaperTable(tables.Table):
    class Meta:
        model = ColorectalCancerPaper
        template_name = "django_tables2/bootstrap.html"

class ColorectalCancerMetTable(tables.Table):
    class Meta:
        model = ColorectalCancerMet
        template_name = "django_tables2/bootstrap.html"

class ColorectalCancerTherTable(tables.Table):
    class Meta:
        model = ColorectalCancerTher
        template_name = "django_tables2/bootstrap.html"

class ColorectalCancerTherPublTable(tables.Table):
    class Meta:
        model = ColorectalCancerTherPubl
        template_name = "django_tables2/bootstrap.html"




class ArthritisCancerTherTable(tables.Table):
    class Meta:
        model = ArthritisCancerTher
        template_name = "django_tables2/bootstrap.html"

class ArthritisCancerTherPublTable(tables.Table):
    class Meta:
        model = ArthritisCancerTherPubl
        template_name = "django_tables2/bootstrap.html"




class DepressionCancerTherTable(tables.Table):
    class Meta:
        model = DepressionCancerTher
        template_name = "django_tables2/bootstrap.html"

class DepressionCancerTherPublTable(tables.Table):
    class Meta:
        model = DepressionCancerTherPubl
        template_name = "django_tables2/bootstrap.html"




class CvdCancerTherTable(tables.Table):
    class Meta:
        model = CvdCancerTher
        template_name = "django_tables2/bootstrap.html"

class CvdCancerTherPublTable(tables.Table):
    class Meta:
        model = CvdCancerTherPubl
        template_name = "django_tables2/bootstrap.html"




#########OURS


class CvdCancerOursTable(tables.Table):
    class Meta:
        model = CvdCancerOurs
        template_name = "django_tables2/bootstrap.html"
