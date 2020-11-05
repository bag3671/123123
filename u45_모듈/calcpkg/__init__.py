# __init__.py 파일은 내용을 비워 둘 수 있음
#이 파일이 있으면 자동으로 폴더를 패키지로 인식

#최초는 빈파일

#두번째
#from . import operation    # 현재 패키지에서 operation 모듈을 가져옴
#from . import geometry     # 현재 패키지에서 geometry 모듈을 가져옴

#세번째
from .operation import *    
from .geometry import *     