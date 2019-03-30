#모듈의 경로
"""
1. 스크립트가 들어 있는 디렉토리
2. PYTHONPATH
3. 표준라이브러리 디렉토리(ex -> c:\python36\lib)
sys.path.append('추가할경로')
sys.path.remove('제거할경로')
"""
import ex.sam
import sys
print(dir(ex.sam))
print('-'*20)
print(sys.path)