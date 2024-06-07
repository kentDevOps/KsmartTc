import pytest
import os
import sys

def main():
    cc = os.path.dirname(__file__)
    current_directory = os.path.join(cc,'vd','test_vd.py')  
    # Xác định đường dẫn tới file test trong môi trường đã đóng gói
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".") 
    pytest.main([current_directory])     
    input('kkk')
if __name__ == "__main__":
    main()