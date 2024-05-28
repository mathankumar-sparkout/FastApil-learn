# QuaryParameter----------------------------


from fastapi import FastAPI  # -> import api
from typing import Union  # -> union use quary parameter

app = FastAPI()

Union[str, int] or int | str
@app.get(
    "/root/{p_id}"
)  # -> path parameter(p_id) #->quary parameter no need to mention path parameter side
def fun(
    p_id: int, id: int, page: Union[int, None] = None
):  # -> p_id int path parameter --> ? id =int  --> ? page not mentioned default value null worked
    return {"page is": page, "id": id, "page_id": p_id}  # -> return the values


# ----------------------------------------------------------------------------------------------------


@app.get("/{loc}")
def fun(id: int, loc: str, age: Union[int, None] = None):
    return {"age is": age, "id": id, "loc": loc}
