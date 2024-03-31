# Simple errors as values for Python

```python
from simple_err import trying, wrap_in_trying
import business_logic
import operator as op


safe_div = wrap_in_trying(op.truediv)

result = safe_div(5, 0)

if isinstance(result, ZeroDivisionError):
    result = 0

business_logic.complex_function(result)
```