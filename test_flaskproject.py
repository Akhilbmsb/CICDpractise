from flaskproject import add,sub,mult,div,sqrt,cod

def test_add():
    result=add(-2,-3)
    assert result == -5
    
def test_sub():
    result=sub(-2,-3)
    assert result == 1
    
def test_mult():
    result=mult(2,3)
    assert result == 6
    
def test_div():
    result=div(2,0)
    assert result == "infinity"
    
def test_sqroot():
    result=sqrt(4)
    assert result == 2

def test_cod():
    result=cod(1)
    assert result == "1"
