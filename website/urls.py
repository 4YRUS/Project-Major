from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home' ),
    path('work1/',views.work1,name='work1' ),
    path('pdf-extraction/<int:pk>/',views.pdfExtraction,name='PdfExtraction' ),
    path('pdf-extraction-home/',views.pdfExtractionHome,name='PdfExtractionHome' ),
    path('mcq-test-home/',views.mcqTestHome,name='mcqTestHome' ),
    path('fetch/',views.forfetch,name="fetch"),
    path('read/',views.read_canvas,name="read"),
    path('canvasResponse/',views.return_canvas_response,name="canvas"),
    path('extracted-data/<int:pk>/',views.extractedData,name="ExtractedData"),
    path('extract-data/',views.extractData,name="ExtractData"),
    path('extract-mcqs/',views.extractMcqs,name="ExtractMcqs"),
    path('topic-data/',views.getTopics,name="GetTopics"),
    path('pdf-data/',views.getPdfs,name="GetPdfs"),
    path('mcq-test/',views.mcqTest,name="McqTest"),
    path("extract-existing-pdfs/<int:pk>/",views.extractExistingPdf,name="ExtractExistingPdfs"),

]
